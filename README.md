# PLP-Python-assignment-wk-5-OOP
Here’s a clean and beginner-friendly **README** for your Python OOP assignment, Mwenda. It explains what the code does, how it works, and how to run it—perfect for submission or sharing with others.

---

## 📱 Smartphone Class – Python OOP Assignment

### 🧾 Overview
This Python program demonstrates **Object-Oriented Programming (OOP)** concepts using a `Smartphone` class and a subclass `SmartphoneWithCamera`. It showcases:
- Class creation
- Constructors (`__init__`)
- Attributes and methods
- Inheritance
- Polymorphism (method overriding)

---

### 🏗️ Structure

#### 1. `Smartphone` Class
Represents a basic smartphone with:
- Attributes: `brand`, `model`, `storage`
- Methods:
  - `call(number)`: Simulates making a call
  - `specs()`: Returns a string describing the phone's specs

#### 2. `SmartphoneWithCamera` Subclass
Extends `Smartphone` by adding:
- Attribute: `camera_megapixels`
- Overridden `specs()` method to include camera details

---

### 🧪 Example Usage
```python
phone1 = Smartphone("Samsung", "Galaxy A14", 128)
phone2 = Smartphone("Apple", "iPhone 13", 256)

print(phone1.specs())  # Output: Samsung Galaxy A14 with 128GB storage
print(phone2.specs())  # Output: Apple iPhone 13 with 256GB storage

phone3 = SmartphoneWithCamera("Google", "Pixel 6", 128, 50)
print(phone3.specs())  # Output: Google Pixel 6 with 128GB storage, Camera: 50MP
```

---

### 🚀 How to Run
1. Save the code in a file named `OOP.py`.
2. Open a terminal or command prompt.
3. Run the file using:
   ```bash
   python OOP.py
   ```

---

### 📚 Concepts Demonstrated
- **Encapsulation**: Each object stores its own data.
- **Inheritance**: `SmartphoneWithCamera` inherits from `Smartphone`.
- **Polymorphism**: The `specs()` method behaves differently in the subclass.

---

### ✅ Requirements
- Python 3.x installed
- No external libraries needed

---

Let me know if you want to add a section for future improvements or turn this into a mini project with user input and storage. We can level it up anytime.
