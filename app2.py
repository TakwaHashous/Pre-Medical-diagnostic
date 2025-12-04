import tkinter as tk
from tkinter import messagebox, ttk
from typing import *

class AdvancedSymptomChecker:
    def __init__(self, master):
        self.master = master
        self.master.title(" Medical Symptom Checker")
        self.master.geometry("800x600")
        self.master.configure(bg="#f0f8ff")
        
        # Initialize variables
        self.current_frame = None
        self.selected_gender = None
        self.selected_main_part = None
        self.selected_specific_part = None
        self.responses = {}
        
        self.create_welcome_screen()
        
    def create_welcome_screen(self):
        self.clear_current_frame()
        
        frame = tk.Frame(self.master, bg="#f0f8ff")
        frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Welcome message
        tk.Label(
            frame,
            text="Welcome to the Advanced Medical Symptom Checker",
            font=("Arial", 24, "bold"),
            bg="#f0f8ff",
            wraplength=700
        ).pack(pady=20)
        
        tk.Label(
            frame,
            text="Please note: This is not a substitute for professional medical advice. "
                 "If you're experiencing severe symptoms, seek immediate medical attention.",
            font=("Arial", 12),
            bg="#f0f8ff",
            wraplength=600,
            fg="red"
        ).pack(pady=10)
        
        # Gender selection
        gender_frame = tk.Frame(frame, bg="#f0f8ff")
        gender_frame.pack(pady=20)
        
        tk.Label(
            gender_frame,
            text="Select your gender:",
            font=("Arial", 20),
            bg="#f0f8ff"
        ).pack(pady=10)
        
        for gender in ["Male", "Female"]:
            tk.Button(
                gender_frame,
                text=gender,
                command=lambda g=gender: self.select_gender(g),
                font=("Arial", 14),
                bg="#add8e6",
                width=15
            ).pack(pady=5)
        
        self.current_frame = frame

    def select_gender(self, gender):
        self.selected_gender = gender
        self.show_main_body_parts()

    def show_main_body_parts(self):
        self.clear_current_frame()
        
        frame = tk.Frame(self.master, bg="#f0f8ff")
        frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        tk.Label(
            frame,
            text="Select the main area of concern:",
            font=("Arial", 20, "bold"),
            bg="#f0f8ff"
        ).pack(pady=20)
        
        main_parts = {
            "Head": "#FFB6C1",
            "Chest": "#98FB98",
            "Abdomen": "#87CEEB",
            "Hands": "#DDA0DD",
            "Feet": "#F0E68C",
            "Back": "#E6E6FA",
            "Pelvis": "#FFB6C1"
        }
        
        for part, color in main_parts.items():
            tk.Button(
                frame,
                text=part,
                command=lambda p=part: self.select_main_part(p),
                font=("Arial", 14),
                bg=color,
                width=20
            ).pack(pady=5)
        
        self.current_frame = frame

    def select_main_part(self, main_part):
        self.selected_main_part = main_part
        self.show_specific_parts()

    def show_specific_parts(self):
        self.clear_current_frame()
        
        frame = tk.Frame(self.master, bg="#f0f8ff")
        frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        specific_parts = self.get_specific_parts()
        
        tk.Label(
            frame,
            text=f"Select the specific area of {self.selected_main_part}:",
            font=("Arial", 20, "bold"),
            bg="#f0f8ff"
        ).pack(pady=20)
        
        # Create scrollable frame for specific parts
        canvas = tk.Canvas(frame, bg="#f0f8ff")
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#f0f8ff")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        for part in specific_parts:
            tk.Button(
                scrollable_frame,
                text=part,
                command=lambda p=part: self.select_specific_part(p),
                font=("Arial", 14),
                bg="#E0FFFF",
                width=30
            ).pack(pady=5)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        self.current_frame = frame

    def select_specific_part(self, specific_part):
        self.selected_specific_part = specific_part
        self.show_questions()

    def show_questions(self):
        self.clear_current_frame()
        
        frame = tk.Frame(self.master, bg="#f0f8ff")
        frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Create scrollable frame for questions
        canvas = tk.Canvas(frame, bg="#f0f8ff")
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#f0f8ff")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        tk.Label(
            scrollable_frame,
            text=f"Questions about the {self.selected_specific_part}:",
            font=("Arial", 20, "bold"),
            bg="#f0f8ff"
        ).pack(pady=20)

        questions = self.get_specific_questions()
        self.question_vars = {}
        
        for question in questions:
            var = tk.StringVar(value="No")
            self.question_vars[question] = var
            
            question_frame = tk.Frame(scrollable_frame, bg="#f0f8ff")
            question_frame.pack(fill='x', pady=5)
            
            tk.Label(
                question_frame,
                text=question,
                font=("Arial", 12),
                bg="#f0f8ff",
                wraplength=500
            ).pack(side='left', padx=5)
            
            for option in ["No", "Mild", "Moderate", "Severe"]:
                tk.Radiobutton(
                    question_frame,
                    text=option,
                    variable=var,
                    value=option,
                    bg="#f0f8ff"
                ).pack(side='left', padx=5)

        # Additional symptoms text area
        tk.Label(
            scrollable_frame,
            text="Please describe any other symptoms not mentioned above:",
            font=("Arial", 12),
            bg="#f0f8ff"
        ).pack(pady=10)
        
        self.additional_symptoms = tk.Text(scrollable_frame, height=4, width=50)
        self.additional_symptoms.pack(pady=10)
        
        tk.Button(
            scrollable_frame,
            text="Analyze Symptoms",
            command=self.analyze_symptoms,
            font=("Arial", 14),
            bg="#90EE90",
            width=20
        ).pack(pady=20)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        self.current_frame = frame

    def analyze_symptoms(self):
        # Collect responses
        responses = {q: v.get() for q, v in self.question_vars.items()}
        additional = self.additional_symptoms.get("1.0", tk.END).strip()
        
        # Calculate severity
        severity_scores = {"No": 0, "Mild": 1, "Moderate": 2, "Severe": 3}
        total_score = sum(severity_scores[response] for response in responses.values())
        max_possible = len(responses) 
        
        if total_score == 0:
            severity = "Low"
        elif total_score < max_possible :
            severity = "Mild"
        elif total_score < max_possible  :
            severity = "Moderate"
        else:
            severity = "High"

        # Get specialist and advice
        specialist = self.get_specialist()
        advice = self.get_advice(severity)
        
        # Create detailed report
        report = f"""Medical Symptom Analysis Report
        
Patient Information:
- Gender: {self.selected_gender}
- Main Body Part: {self.selected_main_part}
- Specific Area: {self.selected_specific_part}

Symptom Assessment:
"""
        for question, response in responses.items():
            if response != "No":
                report += f"- {question}: {response}\n"
        
        if additional:
            report += f"\nAdditional Symptoms:\n{additional}\n"
        
        report += f"""
Assessment Results:
- Severity Level: {severity}
- Recommended Specialist: {specialist}

Medical Advice:
{advice}

IMPORTANT: This is not a diagnosis. Please consult with a healthcare professional for proper medical evaluation."""

        # Show report in a new window
        report_window = tk.Toplevel(self.master)
        report_window.title("Symptom Analysis Report")
        report_window.geometry("600x800")
        
        text_widget = tk.Text(report_window, wrap=tk.WORD, padx=20, pady=20)
        text_widget.pack(expand=True, fill='both')
        text_widget.insert("1.0", report)
        text_widget.config(state='disabled')
        
        # Add print button
        tk.Button(
            report_window,
            text="Print Report",
            command=lambda: self.print_report(report),
            font=("Arial", 12)
        ).pack(pady=10)

    def get_specific_parts(self) -> List[str]:
        parts_dict = {
            "Head": ["Skull", "Brain", "Eyes", "Ears", "Nose", "Mouth", "Hair", "Neck"],
            "Chest": ["Heart", "Lungs", "Ribs", "Chest Muscles", "Skin"],
            "Abdomen": ["Stomach", "Intestines", "Liver", "Abdominal Muscles", "Skin"],
            "Hands": ["Fingers", "Thumb", "Palm", "Wrist", "Skin"],
            "Feet": ["Toes", "Heel", "Arch", "Sole", "Ankle"],
            "Back": ["Spine", "Shoulder Blades", "Back Muscles", "Skin"],
            "Pelvis": ["Hip Bones", "Bladder", "Reproductive Organs", "Pelvic Muscles", "Skin"]
        }
        return parts_dict.get(self.selected_main_part, [])

    def get_specific_questions(self) -> List[str]:
        # This is a simplified version - in a real application, you'd want a more comprehensive database
        questions_dict = {
            "Brain": [
                "Do you experience headaches?",
                "Have you noticed any memory problems?",
                "Do you have difficulty concentrating?",
                "Have you experienced any seizures?",
                "Do you feel dizzy or lightheaded?"
            ],
            "Eyes": [
                "Do you have blurred vision?",
                "Are your eyes sensitive to light?",
                "Do you see floating spots?",
                "Do you experience eye pain?",
                "Have you noticed any changes in your vision?"
            ],
            # Add more specific questions for each body part...
        }
        
        # Default questions if specific part not found
        default_questions = [
            f"Do you experience pain in your {self.selected_specific_part}?",
            f"Have you noticed any swelling in your {self.selected_specific_part}?",
            f"Is there any numbness or tingling in your {self.selected_specific_part}?",
            f"Have you experienced any limitation of movement in your {self.selected_specific_part}?",
            f"Are there any visible changes in your {self.selected_specific_part}?"
        ]
        
        return questions_dict.get(self.selected_specific_part, default_questions)

    def get_specialist(self) -> str:
        specialist_dict = {
            "Brain": "Neurologist",
            "Eyes": "Ophthalmologist",
            "Ears": "Otolaryngologist (ENT)",
            "Heart": "Cardiologist",
            "Lungs": "Pulmonologist",
            "Stomach": "Gastroenterologist",
            "Liver": "Hepatologist",
            "Spine": "Orthopedist or Neurosurgeon",
            "Hip Bones": "Orthopedist",
            "Reproductive Organs": "Gynecologist or Urologist"
        }
        return specialist_dict.get(self.selected_specific_part, "General Practitioner")

    def get_advice(self, severity: str) -> str:
        advice_dict = {
            "Low": "Monitor your symptoms. Maintain a healthy lifestyle with proper rest and nutrition. If symptoms persist for more than a week, consult your primary care physician.",
            "Mild": "Consider scheduling an appointment with your primary care physician for evaluation. In the meantime, avoid activities that worsen symptoms.",
            "Moderate": "Schedule an appointment with the recommended specialist soon. Until then, rest the affected area and avoid strenuous activities.",
            "High": "Seek immediate medical attention. Consider visiting an emergency room or urgent care facility if symptoms are severe or worsening rapidly."
        }
        return advice_dict.get(severity, "Please consult with a healthcare provider for proper evaluation.")

    def clear_current_frame(self):
        if self.current_frame:
            self.current_frame.destroy()

    def print_report(self, report: str): 
        # In a real application, you'd implement proper printing functionality
        messagebox.showinfo("Print", "Printing functionality would be implemented here.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AdvancedSymptomChecker(root)
    root.mainloop()