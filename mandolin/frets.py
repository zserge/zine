FRETS = [
        ["G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G"],
        ["D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D"],
        ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A"],
        ["E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E"],
]

print("""<svg width="80" height="262" viewBox="0 0 80 262" style="font-family: sans-serif; font-size: 7px;" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    <line x1="10" y1="20" x2="10" y2="260" stroke="black" stroke-width="1" />
    <line x1="30" y1="20" x2="30" y2="260" stroke="black" stroke-width="1" />
    <line x1="50" y1="20" x2="50" y2="260" stroke="black" stroke-width="1" />
    <line x1="70" y1="20" x2="70" y2="260" stroke="black" stroke-width="1" />
    <rect x="9" y="18" width="62" height="3" fill="black" />
""")
for i in range(13):
    y = (i+1) * 20 
    print(f"""<line x1="10" y1="{y}" x2="70" y2="{y}" stroke="black" stroke-width="1" />""")
for (i, f) in enumerate(FRETS):
    for (j, n) in enumerate(f):
        x = 10 + 20 * i
        y = 10 + 20 * j
        c = "black" if len(n) == 2 else "#888"
        print(f"""<g>
  <circle cx="{x}" cy="{y}" r="7" fill="{c}"></circle>
  <text x="{x}" y="{y}" text-anchor="middle" alignment-baseline="middle" fill="white" dy="0.3">{n}</text>
</g>""")
print("""</svg>""")

