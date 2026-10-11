# Decision-model recommendation: semantic discovery after exact lookup

Date: 2026-10-11. Public-source proposal; no model calls.
Reviewed [README](https://github.com/Ethical-Tech-CoLab/cyber-dictionary/blob/fb6aaec8292a5d6eb10eac903fd616d1e7844019/README.md).
Assessment is README-led; generated counts are not repeated as fixed facts.

## Recommendation

Keep synonyms, exact lookup and generated counts deterministic. Test optional
natural-language query-to-entry or query-to-data-source relevance **after**
existing retrieval. Return relevant / related / irrelevant / unknown, or a
defined pointwise ranking rubric, then sort in code.

Source-category suggestions could help editors, but must not infer a dataset's
license, access permission or suitability from its name. Classification labels
and personal-data rules are definitions, not model-authorized access controls.

## Evaluation and alternatives

Compare unchanged search, lexical/fuzzy methods and a licensed local
cross-encoder with Jev's [reranking pattern](https://docs.typesafe.ai/cookbooks/rerank_typesafe.md),
Microsoft-Decision-1 and Sage on public catalogue data.
No need to forward private queries or secrets during an initial trial.

Use query-family-disjoint tests with abbreviations, overloaded terms, misspelling,
multilingual wording and no-fit queries. Measure candidate recall, MRR/NDCG,
wrong-definition selection, unknown rate, latency and accepted-query cost.
Reranking cannot recover entries missing from candidate retrieval.

## Gate

No definition rewriting, permission inference or fabricated API capability.
Keep source/licensing notes and exact search available without a model.
Any browser integration needs protected server-side credentials or a genuinely
local model. Exact Jev/Microsoft/Sage proprietary checkpoints are not available
for local inference. Adopt only if user-search benefit justifies added cost.
