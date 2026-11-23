# Prompt library

Copy the block, fill `<angle brackets>`, delete what does not apply. Keep prompts short
and constrained — one goal, one output shape.

## 1. Spec (before code)

Use when the task is bigger than a one-file fix.

```
Goal: <one sentence>
Users: <who, what they do today>
In scope: <bullets>
Out of scope: <bullets>
Constraints: <stack, conventions, performance, deadline>
Acceptance: <how we know it works — observable behavior>
Open questions: <list, or "none">
Do not write code yet. Return the spec, the file list you expect to touch, and the riskiest assumption.
```

## 2. Plan

```
Read <files/dirs>. Return an ordered plan:
1. <step> → verify: <command or check>
2. ...
Max 6 steps. Flag any step that touches auth, data, or migrations. No code.
```

## 3. Implement (smallest diff)

```
Implement step <n> only.
- Files allowed: <list>. Do not touch anything else.
- Match the conventions in <file>.
- No new dependencies. No abstractions beyond this change.
- After editing, run: <command>. Paste real output.
```

## 4. Test first

```
Write a failing test for <behavior> in <test file>. Do not change source yet.
Show the test and the failure output. Then stop.
```

## 5. Review my diff

```
Review `git diff` as a senior reviewer who did not write it.
Report only defects, each as: file:line — problem — why it matters — concrete fix.
Check: correctness, error paths, input validation, secrets, race/async bugs,
error handling that prevents data loss, missing tests.
No praise, no style nitpicks, no rewrite of untouched code.
```

## 6. Debug

```
Symptom: <exact error + when it happens>
Expected: <...>
Already ruled out: <...>
Do not propose a fix yet. List 3 hypotheses ranked by likelihood, and the
single cheapest observation that would confirm or kill each one.
```

## 7. Commit / PR

```
Write a commit message for this diff.
Subject: imperative, <= 60 chars, no prefix beyond conventional type.
Body: why, not what. Bullet the user-visible changes and any migration/rollback note.
No emojis, no "generated with" footer.
```

## 8. Refactor

```
Refactor <target> without changing behavior.
- Preserve public signatures and output.
- Run <test command> before and after; both must pass.
- Net line count should drop or stay flat.
- Stop and report if a behavior change is unavoidable.
```
