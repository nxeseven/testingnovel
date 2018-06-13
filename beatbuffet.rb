use_bpm 60

a = 8888888 #start universe, likely to be externally controlled

parlel_verse_inc = 1000000000 #parallel universe increment, likely to be externally controlled
synth_plus = 0
scale_plus = 0 #increments through type (list of scale_names)
note_plus = 0 #increments through all keys on piano
sound_plus = 0
b = 3 #oct expansion, universal synth controller
c = (ring :C2, :Cs2, :D2, :Ds2, :E2, :F2, :Fs2, :G2, :Gs2, :A2, :As2, :B2)

type = (ring :major_pentatonic,:chinese,:yu,:minor_pentatonic)#,:yu)
swing = 0.25 # echo phase
d = 0.3 # echo mix, 1 is max mixed
wah_mix = 0.2 #wah effect covers all synths
wah_phase = 2 #wah effect covers all synths

synth_list_a = (ring :fm, :blade, :pluck, :piano, :sine, :pretty_bell,:prophet,:saw,:tri,:supersaw,:mod_sine,:zawa)
synth_list_b = synth_list_a
synth_list_c = synth_list_a


mel_length = 1
bars_delight = 16#bars before universe change
changeup = 2 #multiplies repition and organizes the octave expansion portion, default less than more keys
key_multiple = 1 #how fast are the melodies played
first_timing = 1*key_multiple

first_long = 4*mel_length
second_timing = 0.5*key_multiple

second_long = 8*mel_length
third_timing = 0.125*key_multiple

third_long = 16*mel_length

kick_level = 10
kick_sound = (ring :drum_bass_hard,:bd_808, :bd_ada, :bd_boom, :bd_fat, :bd_gas,
              :bd_haus, :bd_klub, :bd_pure, :bd_sone, :bd_tek, :bd_zome, :bd_zum, :drum_bass_hard,
              :drum_bass_soft)
snare_level = 9
snare_sound = (ring :elec_lo_snare, :elec_mid_snare, :elec_hi_snare, :drum_snare_hard,
               :drum_snare_soft, :elec_filt_snare, :sn_dolf, :sn_dub,  :sn_zome)
snare_job_level = 1
snare_job_sound = (ring :perc_snap,:tabla_dhec, :tabla_ghe1, :tabla_ghe2, :tabla_ghe3, :tabla_ghe4,
                   :tabla_ghe5, :tabla_ghe6, :tabla_ghe7, :tabla_ghe8, :tabla_ke1, :tabla_ke2,
                   :tabla_ke3, :tabla_na, :tabla_na_o, :tabla_na_s, :tabla_re, :tabla_tas1,
                   :tabla_tas2, :tabla_tas3, :tabla_te1, :tabla_te2, :tabla_te_m, :tabla_te_ne,
                   :tabla_tun1, :tabla_tun2, :tabla_tun3)
tap_level = 5
tap_sound = (ring :drum_cymbal_closed, :drum_cymbal_pedal) #constant
tap_sound2 = (ring :drum_cymbal_closed,:elec_blip, :elec_blip2) #tricked out

live_loop :zero do
  #use_bpm e
  if b == 3
    #e = 60
    puts "mel 1"
    mel_length = 1
    first_long = 4*mel_length
    third_long = 16*mel_length
    second_long = 8*mel_length
    sleep bars_delight
    mel_length = 1
    first_long = 4*mel_length
    third_long = 16*mel_length
    second_long = 8*mel_length
    b = 4
    
  else
    
    puts "mel 2"
    mel_length = 1
    first_long = 4*mel_length
    third_long = 16*mel_length
    second_long = 8*mel_length
    sleep bars_delight/2
    
    sleep bars_delight/4
    mel_length = 2
    first_long = 4*mel_length
    third_long = 16*mel_length
    second_long = 8*mel_length
    sleep bars_delight/4
    b = 3
    
  end
  
end

live_loop :changeup do
  
  sleep bars_delight * changeup
  sample :ambi_lunar_land, amp: 2, rate: 1
  a = a + parlel_verse_inc
  synth_plus = synth_plus + 1
  scale_plus = scale_plus + 1
  note_plus = note_plus + 1
  sound_plus = sound_plus + 1
  
end

live_loop :first do
  
  use_random_seed a
  with_fx :ixi_techno, phase: wah_phase, mix: wah_mix do
    with_fx :echo, mix: d, phase: swing do
      first_long.times do
        use_synth synth_list_a[synth_plus]
        play scale(c[note_plus], type[scale_plus], num_octaves: b).shuffle.take(1),
          release: first_timing, amp: rrand(0.25,1), vibrato_rate: choose([5, 10]),
          vibrato_onset: 0.1, vibrato_delay: 0.5#rrand(6,10)#first_level[vel_plus]
        #puts synth_plus
        #puts scale_plus
        #puts a
        #puts synth_list_a[synth_plus]
        #puts type[scale_plus]
        #puts c[note_plus]
        sleep first_timing
        vel_plus = vel_plus + 1
      end
    end
  end
  
end

live_loop :second do
  use_random_seed a #+ 1
  with_fx :ixi_techno, phase: wah_phase, mix: wah_mix do
    with_fx :echo, mix: d, phase: swing do
      second_long.times do
        use_synth synth_list_b[synth_plus]
        play scale(c[note_plus], type[scale_plus], num_octaves: b).shuffle.take(1),
          release: second_timing, amp: rrand(0.95,1), vibrato_rate: choose([5, 10]),
          vibrato_onset: 0.1, vibrato_delay: 0.5#rrand(6,10)#second_level[vel_plus]
        sleep second_timing
        vel_plus = vel_plus + 1
      end
    end
  end
  
end

live_loop :third do
  
  use_random_seed a #+ 2
  with_fx :ixi_techno, phase: wah_phase, mix: wah_mix do
    with_fx :echo, mix: d, phase: swing do
      third_long.times do
        use_synth synth_list_c[synth_plus]
        play scale(c[note_plus], type[scale_plus], num_octaves: b).shuffle.take(1),
          release: third_timing, amp: rrand(0.25,1), vibrato_rate: choose([5, 10]),
          vibrato_onset: 0.1, vibrato_delay: 0.5#rrand(6,10)#third_level[vel_plus]
        
        sleep third_timing
        vel_plus = vel_plus + 1
      end
    end
  end
  
end

uplift = 0
insert = 0
rapid = 0

live_loop :snr do
  #use_bpm e
  uplift += 1
  use_random_seed uplift
  snare_job = choose([8.0,2.0,1.0,3.0,6.0,4.0])
  snare_pattern = [
    1,3,5,7,9,11,13,15,
    2.25,8.25,14.25
  ]
  at snare_pattern do
    with_fx :reverb do
      sample snare_sound[sound_plus], amp: (ring snare_level, 0)[uplift], finish: 0.08
    end
    
    snare_job.times do
      sample snare_job_sound[sound_plus], amp: (ring rrand(0,snare_job_level), 0)[uplift], finish: 0.2, rate: choose([1.0,1.1])
      sleep 1.0/snare_job
    end
  end
  tap_job = choose([8.0,4.0,6.0])
  tap_pattern = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
  at tap_pattern do
    sample tap_sound[sound_plus], amp: (ring rrand(0.1,tap_level), rrand(0.1,tap_level))[uplift], finish: 0.4 #(ring tap_level, tap_level)[uplift],
    
    tap_job.times do
      sample tap_sound2[sound_plus], amp: (ring rrand(0.1,tap_level),0)[uplift], finish: rrand(0.1,0.5) #(ring tap_level, 0)[uplift]
      sleep 1.0/tap_job
    end
  end
  
  
  kp1 = [0,0.25,8,8.125,8.25,8.50,12,12.25,13.75,14.25,15,15.125,15.25,15.5,15.75]
  kp2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
  
  
  kick_pattern = choose([kp1,kp2])
  at kick_pattern do
    sample kick_sound[sound_plus], amp: (ring kick_level, 0)[uplift]
  end
  at kick_pattern do
    sample :bd_ada, amp: (ring kick_level, 0)[uplift]
  end
  sleep 16
end

























