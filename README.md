# Testing

## URL for api

https://serverless-functions-roan.vercel.app/api/adj_synonyms?word=<word>

## How it works

- if the word given is an adjective it will return a list of synonyms for that word
- `https://serverless-functions-roan.vercel.app/api/adj_synonyms?word=amazing` would return `['astonishing', 'astounding', 'surprising', 'bewildering', 'stunning', 'staggering', 'shocking', 'startling', 'stupefying', 'breathtaking', 'perplexing', 'confounding', 'dismaying', 'disconcerting', 'shattering', 'awesome', 'awe-inspiring', 'sensational', 'remarkable', 'spectacular', 'stupendous', 'phenomenal', 'prodigious', 'extraordinary', 'incredible', 'unbelievable', 'wonderful', 'marvellous', 'thrilling', 'exciting', 'mind-blowing', 'flabbergasting', 'amazeballs', 'wondrous', 'dumbfounding']`
- `https://serverless-functions-roan.vercel.app/api/adj_synonyms` would return `no word given`

