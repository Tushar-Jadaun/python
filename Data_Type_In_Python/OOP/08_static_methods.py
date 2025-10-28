class ChaiUtils:
    @staticmethod
    def clean_ingredients(text):
        return [ items.strip() for items in text.split(",")]
    
    
raw = " water,milk,ginger,honey"    
cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned)
