def get_monthly_total(expenses, month_str):
    """month_str format: 'YYYY-MM'"""
    return sum(e.amount for e in expenses if e.date.startswith(month_str))

def get_category_breakdown(expenses):
    breakdown = {}
    for e in expenses:
        breakdown[e.category] = breakdown.get(e.category, 0) + e.amount
    return breakdown

def generate_text_chart(data_dict):
    if not data_dict: return
    max_val = max(data_dict.values())
    print("\n--- Visual Breakdown ---")
    for key, val in data_dict.items():
        bar_length = int((val / max_val) * 20)
        print(f"{key:<12} | {'█' * bar_length} ${val:.2f}")