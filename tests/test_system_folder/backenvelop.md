# Intelligent Triage System Architecture

## Overview
Design a triage system that accepts user input, analyzes it using GPT-4o API, and routes users to the most appropriate service.

## System Requirements
- Accept user input (text)
- Call GPT-4o API for intelligent classification
- Route users to appropriate services based on classification
- **Response Time**: < 500ms end-to-end
- **Scalability**: Handle 1M+ requests per day
- **Accuracy**: 95%+ correct routing decisions

## Scale Estimation

### Traffic & Storage
```
Users: 1,000,000 active users
Daily requests: 20 per user = 20M requests/day
QPS: 20M / 86400 = ~231 req/s (avg), ~700 req/s (peak)
Storage: ~15TB (3 years retention)
Bandwidth: ~1.6MB/s average, ~5MB/s peak
```

## Architecture

```
Client → Load Balancer → API Gateway → Input Processor
                                            ↓
Triage Service ← Request Queue ←────────────┘
      ↓
GPT-4o API + Cache Layer + Router Service
      ↓
Service A (Support) | Service B (Tech) | Service C (Billing)
```

## Core Components

### GPT-4o Integration
```python
async def classify_request(self, input_data) -> TriageDecision:
    # Check cache first (70% hit rate)
    cached = await self.cache.get(cache_key)
    if cached: return cached
    
    # GPT-4o API call (<300ms)
    response = await self.client.chat.completions.create(
        model="gpt-4o",
        messages=self.build_prompt(input_data),
        max_tokens=150,
        timeout=250
    )
    
    decision = self.parse_response(response)
    await self.cache.set(cache_key, decision, ttl=3600)
    return decision
```