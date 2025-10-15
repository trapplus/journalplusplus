class maskString:
    @staticmethod
    def _mask_str (string: str) -> str | None:
            if string:
                masked_jwt = ".".join(part[:7] + "*" * (len(part) - 7) for part in string.split("."))
                if masked_jwt:
                    return masked_jwt
            return None
