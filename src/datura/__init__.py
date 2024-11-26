def flatten_dict(d: dict) -> dict | None:
    # Flatten dict method can only process dicts, abort for any other input.
    if not isinstance(d, dict):
        return d

    ret = {}
    for k, v in d.items():
        """
        Iterate through the provided dictionary, if the value is a
        dictionary, recurse to flatten that dictionary in the case of multiple layers of nesting.
        """
        if isinstance(v, dict):
            for ik, iv in flatten_dict(v).items():
                """
                For every key in the nested dictionary build a new key in the
                format `key.innerkey`. Nested keys will already be in `.`
                notation.
                """
                ret[f"{k}.{ik}"] = iv
        else:
            """
            For all other values maintain the existing key, value pair
            """
            ret[k] = v

    return ret
