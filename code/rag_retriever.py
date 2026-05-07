import numpy as np
import faiss
from typing import List, Dict
from sentence_transformers import SentenceTransformer

ALPHA, BETA = 0.6, 0.4
model = SentenceTransformer('all-MiniLM-L6-v2')

class RAGRetriever:
    def __init__(self, knowledge_base: List[Dict]):
        self.kb = knowledge_base
        self.embeddings = model.encode([kb['text'] for kb in knowledge_base])
        self.index = faiss.IndexFlatL2(self.embeddings.shape[1])
        self.index.add(self.embeddings.astype('float32'))
        
    def retrieve(self, query: str, k: int = 5) -> List[Dict]:
        q_vec = model.encode([query]).astype('float32')
        D, I = self.index.search(q_vec, k * 2)
        
        candidates = []
        for idx, dist in zip(I[0], D[0]):
            if idx < len(self.kb):
                sim_sem = 1 - (dist / 2)  # cosine approx
                risk = self.kb[idx]['risk']
                score = ALPHA * sim_sem + BETA * (1 / (1 + risk))
                candidates.append((self.kb[idx], score))
                
        candidates.sort(key=lambda x: x[1], reverse=True)
        
        # Diversity filter: max 2 from same MITRE tactic
        filtered, tactic_counts = [], {}
        for item, score in candidates:
            t = item['tactic']
            if tactic_counts.get(t, 0) < 2:
                filtered.append((item, score))
                tactic_counts[t] = tactic_counts.get(t, 0) + 1
            if len(filtered) == k: break
        return filtered