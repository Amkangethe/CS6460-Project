# GenAI Feedback Prototype for Programming Education

This project implements a prototype tutoring pipeline that evaluates student code and provides structured feedback using three interaction patterns:

1. Socratic hints
2. Constrained code review
3. Worked examples

The system automatically runs unit tests against student submissions and triggers feedback when failures occur.

## System Pipeline

Student Code → Automated Tests → Feedback Stages

Stage 1: Socratic Hint  
Stage 2: Code Review  
Stage 3: Worked Example  

Each interaction is logged for later analysis.

## How to Run

Run the feedback system:

python ai_feedback/run_feedback.py

Choose a programming task when prompted.

## Project Structure

tasks/  
Reference solutions for programming exercises.

tests/  
Unit tests used to evaluate student submissions.

student_attempts/  
Simulated incorrect student solutions.

ai_feedback/  
Feedback generation pipeline.

## Research Motivation

This prototype explores how structured GenAI feedback patterns may support:

• self-explanation  
• transfer  
• manageable cognitive load during programming practice