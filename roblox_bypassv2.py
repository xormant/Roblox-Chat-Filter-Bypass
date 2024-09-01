import sys
import time

emoji_map = {
    'a': '🅰', 'b': '🅱', 'c': '🅲', 'd': '🅳', 'e': '🅴', 'f': '🅵', 'g': '🅶',
    'h': '🅷', 'i': '🅸', 'j': '🅹', 'k': '🅺', 'l': '🅻', 'm': '🅼', 'n': '🅽',
    'o': '🅾', 'p': '🅿', 'q': '🆀', 'r': '🆁', 's': '🆂', 't': '🆃', 'u': '🆄',
    'v': '🆅', 'w': '🆆', 'x': '🆇', 'y': '🆈', 'z': '🆉',
    '0': '0️⃣', '1': '1️⃣', '2': '2️⃣', '3': '3️⃣', '4': '4️⃣', '5': '5️⃣',
    '6': '6️⃣', '7': '7️⃣', '8': '8️⃣', '9': '9️⃣', ' ': '⬛'
}

def text_to_emoji(input_text):
    return ''.join(emoji_map.get(char.lower(), char) for char in input_text)

def main():
    if len(sys.argv) < 2:
        print("Usage: python example.py <input>")
        return
    
    input_text = ' '.join(sys.argv[1:])
    start_time = time.perf_counter_ns()
    emoji_text = text_to_emoji(input_text)
    
    end_time = time.perf_counter_ns()
    elapsed_time = end_time - start_time
    
    elapsed_time_str = f"{elapsed_time} ɥs"
    
    print(f"Bypassed Text: {emoji_text}")
    print(f"TTS: {elapsed_time_str}")

if __name__ == "__main__":
    main()
