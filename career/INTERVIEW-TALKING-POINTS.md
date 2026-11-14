# Interview discussion guide — Red Team leadership to AI security

**Use:** Prepare for a technical interview. These are prompts for real, supportable experiences—not scripts asserting that a specific confidential event occurred.

## What motivates the AI security transition?

Explain the continuity: nine years in cybersecurity and Red Team leadership → security boundaries, realistic attacker capabilities, evidence collection and hardening → new agent/tool surfaces and AI model lifecycle risks.

Anchor the answer in the real [AI Agent Security Lab experimental evidence](https://github.com/abyilmaz-BatuhanYILMAZ/AI-Agent-Security-Lab/blob/main/docs/MATCHED-MODEL-COMPARISON-2026-11-14.md).

## Why is an agent tool authorization boundary important?

A model can emit a valid-looking tool request in response to lower-trust text. Trusted code should independently authorize the exact action and target. In the currently published **synthetic** dataset, the host gate blocked goal-matching unauthorized simulated actions. That is a bounded software property, not proof of a production agent's security.

## What did the experiment fail to establish?

There were only 15 original synthetic cases and three benign controls; model output validity was weak in multiple conditions. No live production systems, native function-calling provider history or real retrieval index was evaluated. Explain how a larger, blinded test set, better output interface, and true legitimate-workflow utility measures would improve confidence.

## How do your published papers relate?

The 2022 and 2026 papers concern **Android malware classification**, not LLM agent safety. They demonstrate experience communicating ML-for-security studies. Avoid claiming the later paper's 98.4% is a direct improvement over the earlier 92.4% without matched protocols.

## Leadership examples to prepare privately

Select **one genuine, permissioned-to-discuss** example of: defining engagement scope, coordinating across functions, diagnosing a detection gap, proposing remediation, or resolving a difficult technical trade-off. For each, write Situation → Your specific responsibility → Method → Measured result → Lessons. Do not disclose customers, architecture secrets, exploit code, credentials or invented metrics.

## Questions to ask the research program

- What experimental reproducibility standards are expected?
- Are projects evaluated primarily for exploit discovery, control validation, or measurement rigor?
- What safe model endpoints/datasets can research participants use?
- How is the utility–security trade-off assessed?
- Are held-out experiments and failure analysis expected in final reports?
