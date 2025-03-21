# 🐍 entra-caps.py

- Dump Conditional Access Policies using the Microsoft Graph API
- Requires a "Policy.Read.All" Access Token

> [!note]
> "Policy.Read.ConditionlAccess" does not give access to the `https://graph.microsoft.com/v1.0/identity/conditionalAccess/policies` endpoint

```python
python3 entra-caps.py \
--token <access_token> \
--output caps.json
```

> [!tip]
> `cat` the caps.json into your clipboard (`cat caps.json | xclip -selection clipboard`) and generate a PPTX with Merill Fernando's idPowerToys CA: https://idpowertoys.merill.net/ca


