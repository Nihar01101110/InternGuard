from flask import signals

from preProcessing import clean_text

#Predefined set of Lists
URGENT_KEYWORDS = [
    "limited slots", "last date", "apply today", "apply now",
    "hurry", "final chance", "only today", "urgent",
    "deadline today", "closing soon", "slots filling fast",
    "few seats left", "immediate joining", "today only",
    "act fast", "don’t miss this", "register immediately"
]
PAYMENT_KEYWORDS = [
    "registration fee", "pay", "deposit", "processing fee",
    "application fee", "security amount", "course fee",
    "₹", "rs", "rupees", "only 999", "just 499",
    "upi", "gpay", "paytm", "phonepe", "bank transfer",
    "account number", "payment link", "scan qr"
]
GUARANTEE_KEYWORDS = [
    "100% guaranteed", "guaranteed internship",
    "guaranteed placement", "no interview",
    "direct selection", "instant offer",
    "confirmed offer letter", "assured job",
    "fixed stipend", "earn easily", "easy money",
    "no skills required"
]
BENEFIT_KEYWORDS = [
    "earn 50000", "earn 30000", "high stipend",
    "work from home", "wfh",
    "1 hour per day", "part time only",
    "no experience needed", "students only",
    "easy task", "simple work"
]
AUTHORITY_KEYWORDS = [
    "government approved", "iso certified",
    "aictc approved", "ugc approved",
    "official partner", "recognized by govt",
    "mnc company", "fortune company",
    "startup india"
]
CONTACT_KEYWORDS = [
    "contact on whatsapp", "dm me",
    "telegram", "message now",
    "personal number", "direct message",
    "call immediately"
]
LANGUAGE_PATTERNS = [
    "!!!", "!!!", "!!!",
    "limited time offer", "free certificate"
]

