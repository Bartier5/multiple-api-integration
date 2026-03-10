def combine(parsed_data):
    crypto = parsed_data["crypto"]
    space = parsed_data["space"]
    quote = parsed_data["quote"]
    
    has_crypto = "error" not in crypto
    has_space = "error" not in space
    has_quote = "error" not in quote
    return{
        "crypto": crypto if has_crypto else None,
        "space":      space  if has_space  else None,
        "quote":      quote  if has_quote  else None,
        "errors":     {
            k: parsed_data[k]["error"]
            for k in ["crypto", "space", "quote"]
            if "error" in parsed_data[k]
        }
    }
    