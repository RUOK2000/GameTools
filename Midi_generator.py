# This program generates simple random midi files
# This software is released under the GPL-3.0 License
# Written by RUOK, check out www.mbcentertainment.co.uk 

import mido
from mido import MidiFile, MidiTrack, Message
import random

# Constants for the MIDI file
tempo = 120  # Beats per minute
beats_per_bar = 4
bars = 16
ppq = 480  # Pulses (ticks) per quarter note (beat)

# Calculate the total number of ticks for a 16-bar piece
ticks_per_beat = ppq
total_ticks = ticks_per_beat * beats_per_bar * bars

# Create a new MIDI file and add a track
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# Sets the tempo message
track.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(tempo)))

# Add a program change message
track.append(Message('program_change', program=12, time=0))

# Generating 16 bars of random notes
# Choosing notes from the MIDI range 60 (C4) to 72 (C5)
for bar in range(bars):
    for _ in range(beats_per_bar):
        note = random.randint(60, 72)  # Random note between C4 and C5
        velocity = random.randint(50, 100)  # Random velocity for variation

        # Note on
        track.append(Message('note_on', note=note, velocity=velocity, time=0))
        # Duration is one beat (ticks_per_beat)
        track.append(Message('note_off', note=note, velocity=velocity, time=ticks_per_beat))

# Save the MIDI file
output_file = '16_bar_random_melody.mid'
mid.save(output_file)

print(f"16-bar MIDI file with random melody created successfully as '{output_file}'.")