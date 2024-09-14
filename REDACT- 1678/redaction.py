import spacy

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

# Function to perform redaction, masking, or anonymization
def redact_text(text, redaction_type):
    """
    Redact or mask named entities from the text.
    :param text: Input text
    :param redaction_type: 'redact', 'mask', or 'anonymize'
    :return: Processed text
    """
    # Process the text with spaCy NLP pipeline
    doc = nlp(text)
    
    if redaction_type == "redact":
        for ent in doc.ents:
            text = text.replace(ent.text, "[REDACTED]")
    
    elif redaction_type == "mask":
        # Use a dictionary to handle replacements
        replacements = {}
        for ent in doc.ents:
            if len(ent.text) > 2:
                masked = ent.text[0] + "*" * (len(ent.text) - 2) + ent.text[-1]
            else:
                masked = "*" * len(ent.text)
            replacements[ent.text] = masked
        
        for original, replacement in replacements.items():
            text = text.replace(original, replacement)
            
    elif redaction_type == "anonymize":
        for ent in doc.ents:
            text = text.replace(ent.text, f"[ANONYMIZED {ent.label_}]")
    
    return text
