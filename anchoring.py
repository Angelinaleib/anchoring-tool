import random

anker = random.choice([10, 100, 1000])
print("Kurze Frage:")
print(f"Ist die Zahl {anker} eher hoch oder niedrig?")
input("Drücke Enter um weiterzumachen...")

frage = "Wie viele Länder gibt es deiner Meinung nach in Afrika?"
antwort = int(input(frage + " "))

tatsache = 54

print("\nAuflösung:")
print(f"Die richtige Antwort ist ungefähr {tatsache}.")

print("\nWarum das spannend ist:")
print(
    "Studien zeigen, dass hohe Anker zu höheren Schätzungen führen\n"
    "und niedrige Anker zu niedrigeren – selbst wenn sie zufällig sind."
)
