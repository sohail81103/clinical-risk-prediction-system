def validate_features(features, expected_len=19):
    if not isinstance(features, list):
        raise ValueError("Features must be provided as a list.")

    if len(features) != expected_len:
        raise ValueError(f"Expected {expected_len} features, got {len(features)}.")

    for i, val in enumerate(features):
        if not isinstance(val, (int, float)):
            raise ValueError(f"Feature at index {i} is not numeric.")

    return True
