def fallback_email(context, tone, extra):
    templates = {
        "Professional": f"""
Dear Sir/Madam,

I hope this email finds you well. I am writing regarding {context}.
{extra}

Thank you for your time and consideration.

Best regards,
Hemant Jain
""",

        "Formal": f"""
Respected Sir/Madam,

This is to formally inform you about {context}.
{extra}

Yours sincerely,
Hemant Jain
""",

        "Friendly": f"""
Hi,

Hope you’re doing well! Just wanted to connect regarding {context}.
{extra}

Thanks,
Hemant Jain
""",

        "Follow-up": f"""
Dear Sir/Madam,

I hope you are doing well. I am writing to follow up regarding {context}.
{extra}

Looking forward to your response.

Best regards,
Hemant Jain
""",

        "Apology": f"""
Dear Sir/Madam,

I sincerely apologize for {context}.
{extra}

Thank you for your understanding.

Sincerely,
Hemant Jain
""",

        "Request": f"""
Dear Sir/Madam,

I would like to kindly request regarding {context}.
{extra}

Thank you for your support.

Best regards,
Hemant Jain
"""
    }

    return templates.get(tone, "Unable to generate email.")
