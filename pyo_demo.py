from pyo import *


def harms(s):
    # Creates a sine wave as the source to process.
    a = Sine()#.out()

    # Passes the sine wave through an harmonizer.
    h1 = Harmonizer(a)#.out()

    # Then the harmonized sound through another harmonizer.
    h2 = Harmonizer(h1).out()

    # And again...
    h3 = Harmonizer(h2).out()

    # And again...
    h4 = Harmonizer(h3).out()
    s.gui(locals())


def split(s):
    # Creates a source (white noise)
    n = Noise()

    # Sends the bass frequencies (below 1000 Hz) to the left
    lp = ButLP(n).out()

    # Sends the high frequencies (above 1000 Hz) to the right
    hp = ButHP(n).out(1)
    s.gui(locals())


def triangle_wave(s):
    s = Server().boot()
    s.amp = 0.1

    # Sets fundamental frequency
    freq = 200

    # Approximates a triangle waveform by adding odd harmonics with
    # amplitude proportional to the inverse square of the harmonic number.
    h1 = Sine(freq=freq, mul=1).out()
    h2 = Sine(freq=freq*3, phase=0.5, mul=1./pow(3,2)).out()
    h3 = Sine(freq=freq*5, mul=1./pow(5,2)).out()
    h4 = Sine(freq=freq*7, phase=0.5, mul=1./pow(7,2)).out()
    h5 = Sine(freq=freq*9, mul=1./pow(9,2)).out()
    h6 = Sine(freq=freq*11, phase=0.5, mul=1./pow(11,2)).out()

    # Displays the final waveform
    sp = Scope(h1+h2+h3+h4+h5+h6)
    s.gui(locals())


def graphical_parameters(s):
    # Creates two objects with cool parameters, one per channel.
    a = FM().out()
    b = FM().out(1)

    # Opens the controller windows.
    a.ctrl(title="Frequency modulation left channel")
    b.ctrl(title="Frequency modulation right channel")

    # If a list of values is given at a particular argument, the ctrl
    # window will show a multislider to set each value separately.

    oscs = Sine([100, 200, 300, 400, 500, 600, 700, 800], mul=0.1).out()
    oscs.ctrl(title="Simple additive synthesis")

    s.gui(locals())


def mul_and_add(s):
    # The `mul` attribute multiplies each sample by its value.
    a = Sine(freq=100, mul=0.1)

    # The `add` attribute adds an offset to each sample.
    # The multiplication is applied before the addition.
    b = Sine(freq=100, mul=0.5, add=0.5)

    # Using the range(min, max) method allows to automatically
    # compute both `mul` and `add` attributes.
    c = Sine(freq=100).range(-0.25, 0.5)

    # Displays the waveforms
    sc = Scope([a, b, c])

    s.gui(locals())


def lfos(s):
    # Creates a noise source
    n = Noise()

    # Creates an LFO oscillating +/- 500 around 1000 (filter's frequency)
    lfo1 = Sine(freq=.1, mul=500, add=1000)
    # Creates an LFO oscillating between 2 and 8 (filter's Q)
    lfo2 = Sine(freq=.4).range(2, 8)
    # Creates a dynamic bandpass filter applied to the noise source
    bp1 = ButBP(n, freq=lfo1, q=lfo2).out()

    # The LFO object provides more waveforms than just a sine wave

    # Creates a ramp oscillating +/- 1000 around 12000 (filter's frequency)
    lfo3 = LFO(freq=.25, type=1, mul=1000, add=1200)
    # Creates a square oscillating between 4 and 12 (filter's Q)
    lfo4 = LFO(freq=4, type=2).range(4, 12)
    # Creates a second dynamic bandpass filter applied to the noise source
    bp2 = ButBP(n, freq=lfo3, q=lfo4).out(1)

    s.gui(locals())


def arithmetic(s):
    # Full scale sine wave
    a = Sine()

    # Creates a Dummy object `b` with `mul` attribute
    # set to 0.5 and leaves `a` unchanged.
    b = a * 0.5
    b.out()

    # Instance of Dummy class
    print(b)

    # Computes a ring modulation between two PyoObjects
    # and scales the amplitude of the resulting signal.
    c = Sine(300)
    d = a * c * 0.3
    d.out()

    # PyoObject can be used with Exponent operator.
    e = c ** 10 * 0.4
    e.out(1)

    # Displays the ringmod and the rectified signals.
    sp = Spectrum([d, e])
    sc = Scope([d, e])

    s.gui(locals())


def streams(s):
    ### Using multichannel-expansion to create a square wave ###

    # Sets fundamental frequency.
    freq = 100
    # Sets the highest harmonic.
    high = 20

    # Generates the list of harmonic frequencies (odd only).
    harms = [freq * i for i in range(1, high) if i % 2 == 1]
    # Generates the list of harmonic amplitudes (1 / n).
    amps = [0.33 / i for i in range(1, high) if i % 2 == 1]

    # Creates all sine waves at once.
    a = Sine(freq=harms, mul=amps)
    # Prints the number of streams managed by "a".
    print(len(a))

    # The mix(voices) method (defined in PyoObject) mixes
    # the object streams into `voices` streams.
    b = a.mix(voices=1).out()

    # Displays the waveform.
    sc = Scope(b)

    s.gui(locals())


def multichannel_expansion(s):
    # 12 streams with different combinations of `freq` and `ratio`.
    a = SumOsc(freq=[100, 150.2, 200.5, 250.7],
               ratio=[0.501, 0.753, 1.255],
               index=[.3, .4, .5, .6, .7, .4, .5, .3, .6, .7, .3, .5],
               mul=.05)

    # Adds a stereo reverberation to the signal
    rev = Freeverb(a.mix(2), size=0.80, damp=0.70, bal=0.30).out()

    s.gui(locals())


def handling_channels(s):
    # Sets fundamental frequency and highest harmonic.
    freq = 100
    high = 20

    # Generates lists for frequencies and amplitudes
    harms = [freq * i for i in range(1, high) if i % 2 == 1]
    amps = [0.33 / i for i in range(1, high) if i % 2 == 1]

    # Creates a square wave by additive synthesis.
    a = Sine(freq=harms, mul=amps)
    print("Number of Sine streams: %d" % len(a))

    # Mix down the number of streams of "a" before computing the Chorus.
    b = Chorus(a.mix(2), feedback=0.5).out()
    print("Number of Chorus streams: %d" % len(b))

    s.gui(locals())


def handling_channels2(s):
    # Generates a sine wave
    a = Sine(freq=500, mul=0.3)

    # Mixes it up to four streams
    b = a.mix(4)

    # Outputs to channels 0, 2, 4 and 6
    b.out(chnl=0, inc=2)

    s.gui(locals())


def random_multichannel_outputs(s):
    amps = [.05, .1, .15, .2, .25, .3, .35, .4]

    # Generates 8 sine waves with
    # increasing amplitudes
    a = Sine(freq=500, mul=amps)

    # Shuffles physical output channels
    a.out(chnl=-1)

    s.gui(locals())


def complex_spectrum_oscillators(s):
    # Sets fundamental frequency.
    freq = 187.5

    # Impulse train generator.
    lfo1 = Sine(.1).range(1, 50)
    osc1 = Blit(freq=freq, harms=lfo1, mul=0.3)

    # RC circuit.
    lfo2 = Sine(.1, mul=0.5, add=0.5)
    osc2 = RCOsc(freq=freq, sharp=lfo2, mul=0.3)

    # Sine wave oscillator with feedback.
    lfo3 = Sine(.1).range(0, .18)
    osc3 = SineLoop(freq=freq, feedback=lfo3, mul=0.3)

    # Roland JP-8000 Supersaw emulator.
    lfo4 = Sine(.1).range(0.1, 0.75)
    osc4 = SuperSaw(freq=freq, detune=lfo4, mul=0.3)

    # Interpolates between input objects to produce a single output
    sel = Selector([osc1, osc2, osc3, osc4]).out()
    sel.ctrl(title="Input interpolator (0=Blit, 1=RCOsc, 2=SineLoop, 3=SuperSaw)")

    # Displays the waveform of the chosen source
    sc = Scope(sel)

    # Displays the spectrum contents of the chosen source
    sp = Spectrum(sel)

    s.gui(locals())


def pydemo1(s):
    wav = SquareTable()
    beat = Metro(time=0.125, poly=7).play()
    envelope = CosTable([(0, 0), (100, 1), (500, .3), (8191, 0)])
    amplitude = TrigEnv(beat, table=envelope, dur=0.125, mul=0.5)
    pitch = TrigXnoiseMidi(beat, dist=2, scale=5, mrange=(24, 12))

    oscillator = Osc(table=wav, freq=pitch, mul=amplitude).out()

    sig = LinTable([(0, 20), (200, 5), (1000, 2), (8191, 1)])
    metro_synth = Metro(time=0.125, poly=5).play()
    lfo = LFO(freq=4.2, sharp=0.2, type=4, mul=110, add=220)
    envelope_synth = TrigEnv(metro_synth, table=sig, dur=0.5)

    synth = FM(carrier=[220.5, 220], ratio=[.2498, .2503], index=envelope_synth, mul=0.1).out()

    lfd = Sine([0.4, 0.2], mul=0.2, add=0.5)

    synth_80 = SuperSaw(freq=440, detune=lfd, bal=8, mul=0.03).out()
    s.start()
    s.gui(locals())


def pydemo2(s):
    ### signal shape (in this case, a square wave)
    wav = SquareTable()

    ### beat timing
    beat = Metro(time=0.125, poly=7).play()
    # beat = Beat(time=0.125, taps=64, poly=5).play()

    ### amplitude envelope shape
    envelope = CosTable([(0, 0), (100, 1), (500, .3), (8191, 0)])
    # envelope = CurveTable([(0,0),(2048,.5),(4096,.2),(6144,.5),(8192,0)], 0, 20)

    ### amplitude
    amplitude = TrigEnv(beat, table=envelope, dur=0.25, mul=0.6)

    ### random notes
    pitch = TrigXnoiseMidi(beat, dist=3, scale=0, mrange=(24, 24))

    oscillator = Osc(table=wav, freq=pitch, mul=amplitude).out()

    s.gui(locals())


def main():
    s = Server().boot()
    s.amp = 0.1
    # harms(s)
    # split(s)
    # triangle_wave(s)
    # graphical_parameters(s)
    # mul_and_add(s)
    # lfos(s)
    # arithmetic(s)
    # streams(s)
    # multichannel_expansion(s)
    # handling_channels(s)
    # handling_channels2(s)
    # random_multichannel_outputs(s)
    # complex_spectrum_oscillators(s)
    # pydemo1(s)
    pydemo2(s)



if __name__ == '__main__':
    main()