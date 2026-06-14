# Sample Input/Output Demonstrations

This document shows various conversation scenarios with the chatbot, demonstrating all its capabilities.

---

## Scenario 1: Basic Greeting and Exit

```
============================================================
Welcome to the Rule-Based AI Chatbot!
============================================================
I'm here to assist you with basic questions.
Type 'help' to see what I can do, or 'exit' to quit.
============================================================

You: hi
Bot: Hello! How can I help you today?

You: bye

Thank you for chatting with me!
Goodbye! Have a great day!
============================================================
```

---

## Scenario 2: Getting Help

```
============================================================
Welcome to the Rule-Based AI Chatbot!
============================================================
I'm here to assist you with basic questions.
Type 'help' to see what I can do, or 'exit' to quit.
============================================================

You: help
Bot: 
Available Commands:
-------------------
Greetings:
  - hi, hello, hey
  - good morning, good afternoon, good evening

Questions I can answer:
  - what is your name
  - how are you
  - who created you
  - what can you do
  - help

Exit commands:
  - bye, exit, quit, goodbye

Try asking me any of these questions!
        

You: exit

Thank you for chatting with me!
Goodbye! Have a great day!
============================================================
```

---

## Scenario 3: Complete Conversation

```
============================================================
Welcome to the Rule-Based AI Chatbot!
============================================================
I'm here to assist you with basic questions.
Type 'help' to see what I can do, or 'exit' to quit.
============================================================

You: good morning
Bot: Good morning! Hope you're having a wonderful day!

You: what is your name
Bot: I'm a Rule-Based Chatbot, created to assist you with basic queries!

You: how are you
Bot: I'm just a program, but I'm functioning perfectly! Thanks for asking. How are you?

You: who created you
Bot: I was created as part of an AI internship project using Python!

You: what can you do
Bot: I can respond to greetings, answer basic questions about myself, and provide help. Type 'help' to see all available commands!

You: quit

Thank you for chatting with me!
Goodbye! Have a great day!
============================================================
```

---

## Scenario 4: Different Greetings

```
============================================================
Welcome to the Rule-Based AI Chatbot!
============================================================
I'm here to assist you with basic questions.
Type 'help' to see what I can do, or 'exit' to quit.
============================================================

You: hello
Bot: Hello! How can I help you today?

You: good afternoon
Bot: Good afternoon! How can I assist you?

You: hey
Bot: Hello! How can I help you today?

You: good evening
Bot: Good evening! What can I do for you?

You: goodbye

Thank you for chatting with me!
Goodbye! Have a great day!
============================================================
```

---

## Scenario 5: Case Insensitivity Test

```
============================================================
Welcome to the Rule-Based AI Chatbot!
============================================================
I'm here to assist you with basic questions.
Type 'help' to see what I can do, or 'exit' to quit.
============================================================

You: HI
Bot: Hello! How can I help you today?

You: WHAT IS YOUR NAME
Bot: I'm a Rule-Based Chatbot, created to assist you with basic queries!

You: How Are You
Bot: I'm just a program, but I'm functioning perfectly! Thanks for asking. How are you?

You: EXIT

Thank you for chatting with me!
Goodbye! Have a great day!
============================================================
```

---

## Scenario 6: Unknown Input Handling

```
============================================================
Welcome to the Rule-Based AI Chatbot!
============================================================
I'm here to assist you with basic questions.
Type 'help' to see what I can do, or 'exit' to quit.
============================================================

You: what is the weather today
Bot: Sorry, I don't understand that. Please try another question.

You: tell me a joke
Bot: Sorry, I don't understand that. Please try another question.

You: help
Bot: 
Available Commands:
-------------------
Greetings:
  - hi, hello, hey
  - good morning, good afternoon, good evening

Questions I can answer:
  - what is your name
  - how are you
  - who created you
  - what can you do
  - help

Exit commands:
  - bye, exit, quit, goodbye

Try asking me any of these questions!
        

You: what is your name
Bot: I'm a Rule-Based Chatbot, created to assist you with basic queries!

You: bye

Thank you for chatting with me!
Goodbye! Have a great day!
============================================================
```

---

## Scenario 7: Empty Input Handling

```
============================================================
Welcome to the Rule-Based AI Chatbot!
============================================================
I'm here to assist you with basic questions.
Type 'help' to see what I can do, or 'exit' to quit.
============================================================

You: 
Bot: Please enter a message.

You:    
Bot: Please enter a message.

You: hi
Bot: Hello! How can I help you today?

You: exit

Thank you for chatting with me!
Goodbye! Have a great day!
============================================================
```

---

## Scenario 8: All Exit Commands

```
============================================================
Welcome to the Rule-Based AI Chatbot!
============================================================
I'm here to assist you with basic questions.
Type 'help' to see what I can do, or 'exit' to quit.
============================================================

You: hi
Bot: Hello! How can I help you today?

You: bye

Thank you for chatting with me!
Goodbye! Have a great day!
============================================================
```

**Alternative exit commands that also work:**
- `exit`
- `quit`
- `goodbye`

---

## Scenario 9: Typical Internship Demo

```
============================================================
Welcome to the Rule-Based AI Chatbot!
============================================================
I'm here to assist you with basic questions.
Type 'help' to see what I can do, or 'exit' to quit.
============================================================

You: hello
Bot: Hello! How can I help you today?

You: I want to know about you
Bot: Sorry, I don't understand that. Please try another question.

You: what can you do
Bot: I can respond to greetings, answer basic questions about myself, and provide help. Type 'help' to see all available commands!

You: what is your name
Bot: I'm a Rule-Based Chatbot, created to assist you with basic queries!

You: who created you
Bot: I was created as part of an AI internship project using Python!

You: how are you
Bot: I'm just a program, but I'm functioning perfectly! Thanks for asking. How are you?

You: thank you
Bot: Sorry, I don't understand that. Please try another question.

You: exit

Thank you for chatting with me!
Goodbye! Have a great day!
============================================================
```

---

## Performance Characteristics

### Response Time
- **Average**: < 0.01 seconds (instant)
- **No delays**: Responses are immediate
- **Consistent**: Same performance for all inputs

### Memory Usage
- **Minimal**: < 10 MB RAM
- **No accumulation**: No memory leaks
- **Efficient**: Pure Python, no external dependencies

### Input Handling
- **Case-insensitive**: HI = hi = Hi
- **Whitespace-tolerant**: "  hi  " = "hi"
- **Empty input protected**: Prompts user to enter message
- **Infinite loop**: Runs until explicit exit command

---

## Edge Cases Handled

### 1. Mixed Case Input
```
You: HeLLo
Bot: Hello! How can I help you today?
```

### 2. Extra Whitespace
```
You:    hi    
Bot: Hello! How can I help you today?
```

### 3. Empty Messages
```
You: 
Bot: Please enter a message.

You:         
Bot: Please enter a message.
```

### 4. Unknown Commands
```
You: sing a song
Bot: Sorry, I don't understand that. Please try another question.
```

### 5. Partial Matches (Not Supported)
```
You: what's your name
Bot: Sorry, I don't understand that. Please try another question.

[Note: Must be exactly "what is your name"]
```

---

## Testing Checklist

### Basic Functionality
- [x] Greetings work (hi, hello, hey)
- [x] Time-specific greetings work (good morning, etc.)
- [x] Exit commands work (bye, exit, quit, goodbye)
- [x] Help command displays full menu
- [x] Identity questions answered correctly
- [x] Unknown input handled gracefully

### Input Processing
- [x] Case insensitivity works
- [x] Whitespace trimming works
- [x] Empty input rejected politely
- [x] Loop continues until exit

### User Experience
- [x] Welcome message displays on start
- [x] Farewell message displays on exit
- [x] Responses are clear and friendly
- [x] Help provides useful guidance

### Code Quality
- [x] No syntax errors
- [x] No runtime errors
- [x] Functions properly documented
- [x] Comments explain logic
- [x] Code follows PEP 8 style guide

---

## Common Questions from Demos

### Q: Why doesn't "what's your name" work?
**A**: Current implementation requires exact matches. "what is your name" is the exact phrase needed. This can be enhanced with partial matching (see ENHANCEMENTS.md, Level 1.2).

### Q: Can it remember previous messages?
**A**: No, each input is processed independently. Context awareness can be added (see ENHANCEMENTS.md, Level 3.4).

### Q: Why so few responses?
**A**: This is a demonstration of core concepts. It's designed to be extended. The simple structure makes it easy to add more responses without complexity.

### Q: Is this "real AI"?
**A**: This is rule-based AI, using pattern matching and conditional logic. It's a foundation for understanding more advanced AI concepts like machine learning and natural language processing.

---

## How to Run Your Own Tests

### Test Script
Save as `test_chatbot.py`:

```python
from chatbot import get_bot_response

def test_greetings():
    assert "Hello" in get_bot_response("hi")
    assert "morning" in get_bot_response("good morning")
    print("✓ Greetings test passed")

def test_identity():
    response = get_bot_response("what is your name")
    assert "Chatbot" in response
    print("✓ Identity test passed")

def test_exit():
    assert get_bot_response("bye") is None
    assert get_bot_response("exit") is None
    print("✓ Exit test passed")

def test_unknown():
    response = get_bot_response("random gibberish")
    assert "don't understand" in response
    print("✓ Unknown input test passed")

if __name__ == "__main__":
    test_greetings()
    test_identity()
    test_exit()
    test_unknown()
    print("\n✓ All tests passed!")
```

Run with: `python test_chatbot.py`

---

## Conclusion

These samples demonstrate that the chatbot:
1. Handles all required greeting types
2. Responds to all specified questions
3. Accepts all exit commands
4. Provides help when requested
5. Manages unknown input gracefully
6. Processes input case-insensitively
7. Runs continuously until exit
8. Displays appropriate welcome/farewell messages

Perfect for demonstrating fundamental AI concepts in an internship project!
