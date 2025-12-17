"""
Utility Functions Module
"""

def greet(name):
    """ทักทายผู้ใช้"""
    return f"สวัสดี, {name}!"

def calculate_sum(numbers):
    """คำนวณผลรวมของตัวเลข"""
    return sum(numbers)

def calculate_average(numbers):
    """คำนวณค่าเฉลี่ย"""
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)
