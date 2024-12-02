curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer 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" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/Cloudtrio-Ravinadh/testing-/milestones \
  -d '{
    "title": "Release 1.0",
    "description": "First official release milestone.",
    "due_on": "2024-12-31T23:59:59Z"
  }'
