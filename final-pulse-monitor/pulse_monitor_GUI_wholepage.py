#!/usr/bin/python

# Library used for plotting the pulse waveform
import matplotlib

matplotlib.use('TkAgg')
import numpy as np
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import *
from matplotlib.figure import Figure

# Library for GUI
# T is capitalized for python 2.x
# t is lowercase for python 3.x
from Tkinter import *

# Library for progressbar
#from ttk import *

# Grabs data from sensor
#from poll_sensor import *
###     WORKING vvvv (poll_sensor_alt)
#from poll_sensor_alt import *
# Normalized sensor data
from poll_sensor_norm import *
#from temp_poll_sensor import *

# Data/signal processing
from pulse_analysis import *
#from temp_pulse_analysis import *

from pulse_data import *

# Patient Class
from patient import *

# Patient Data File Manager
from file_manager import *

import numpy

# Creates blank window
window = Tk()
window.title("Pulse Monitor Program")
window.resizable(width=True, height=True)
window_width = 1000
window_height = 600
window.minsize(width=window_width, height=window_height)

### Alt. Logic Variables
## Patient Info
name_submitted = 0
period_submitted = 0

## Plot Manipulation
# Full plot [0]     Zoomed in plot[1]
plot_zoomed = 0

### END Alt. Logic Variables

## Patient Data
patient_waveform_raw = []
patient_waveform = []
# Fill patient_waveform with zeros as a placeholder for plot
patient_waveform.append(0)
patient_waveform.append(0)
patient_waveform.append(0)

## File Manager
fm = file_manager()

## END Patient Data

## END Logic Variables

## Functions for disabling/reenabling user input widgets

def patient_name_func():
    print patient_name.get()

def submit_name_button_func():
    global name_submitted, current_patient
    if patient_name.get() == "Enter Patient Name":
        patient_name.set("Enter Patient Name")
    elif fm.check_name(patient_name.get()) == 0:
        patient_name.set("Name Taken")
    else:
        print "Patient Name Submitted"
        print patient_name.get()
        # Initialize Current Patient object
        current_patient = patient(patient_name.get())
        # Disable button and entry textbox
        submit_name_button.config(state='disabled')
        patient_name_entry.config(state='disabled')
        name_submitted = 1
        save_filename.set(patient_name.get().replace(" ", "_"))
        # Set Current Patient's Directory Name
        # --> save_filename is the same as the Patient Directory name
        current_patient.setDirectoryName(save_filename.get())
        print save_filename.get()
        save_patient_data_entry.delete(0, END)
        save_patient_data_entry.insert(0, patient_name.get().replace(" ", "_"))
        # Update Waveform Plot Title
        plot_title = patient_name.get() + " Waveform"
        a.set_title(plot_title, fontsize=14)
        canvas.draw()

def submit_measure_button_func():
    global period_submitted
    if sample_period.get() < 1:
        sample_period.set("Enter value greater than 0")
    else:
        print "Sample Period Submitted"
        print sample_period.get()
        # Disable button and entry textbox
        submit_measure_button.config(state='disabled')
        sample_period_entry.config(state='disabled')
        period_submitted = 1

def start_measure_button_func():
    global patient_waveform, patient_waveform_raw
    # All necessary information was submitted --> pulse measurements starting
    if name_submitted and period_submitted:
        print "Starting pulse monitor..."
        start_measure_button.config(state='disabled')
        take_measurements()
    elif name_submitted and ~period_submitted:
        print "Please submit sample period"
    elif ~name_submitted and period_submitted:
        print "Please submit patient name"
    else:
        print "Please submit patient name and sample period"

def take_measurements():
    global progressbar, progressbar_canvas, patient_pulse_data, patient_waveform, plot_zoomed, start_idx, end_idx
    #progressbar_canvas.itemconfig(progressbar, width=1)
    #progressbar_canvas.itemconfig(progressbar, fill='blue')
    #start_time = time.time()
    #time.sleep(sample_period.get())
    #print start_time
    #print start_time+sample_period.get()
    #print time.time()
    #while time.time() < start_time+sample_period.get():
    #    print round(start_time+sample_period.get()-time.time())
        #increment_progressbar(start_time, time.time())
    print sample_period.get()
#    patient_waveform_raw = poll_for(sample_period.get(), patient_name.get())
    patient_waveform_raw = poll_for(int(sample_period.get()))
    #patient_waveform_raw = poll_for(sample_period.get(), patient_name.get())
    #patient_waveform = pulse_analysis(patient_waveform_raw)
    patient_pulse_data = pulse_analysis(patient_waveform_raw, sample_period.get())
    # Set final processed waveform to be first shown on plot
    patient_waveform = patient_pulse_data.data_final[:]
    # once calculations finish -> enable '(show) plot', 'load plot', 'zoom in' buttons
    show_plot_button.config(state='active')
    load_plot_button.config(state='active')
    zoom_in_button.config(state='active')
    plot_zoomed = 0
    # Set plot start & end indices to start and end of waveform
    start_idx = 0
    end_idx = len(patient_pulse_data.data_final)
    # Update BPM value
    bpm_value_label.config(text=str(patient_pulse_data.bpm))
    set_axis()

def set_axis():
    global patient_pulse_data, s_idx, e_idx, s, e
    n = len(patient_pulse_data.data_final)
    buff = int(round(n/5))
    s_idx = numpy.linspace(0, n-buff, 5)
    e_idx = numpy.linspace(buff, n, 5)
    print s_idx
    print e_idx
    # Default/Initial plot graphs full waveform
    s = 0
    e = 4

# NOT FINISHED - TO BE IMPLEMENTED
def increment_progressbar(start, current):
    global progressbar, progressbar_canvas
    progressbar_canvas.itemconfig(progressbar, width=round(start+sample_period.get()-current))
    progressbar_canvas.draw()

def refresh_plot():
    global patient_waveform, start_idx, end_idx, s_idx, s, e_idx, e
    print "refresh_plot"
    #print int(start_idx)
    #print int(end_idx)
    print s_idx[s]
    print e_idx[e]
    # Adjust axis for start & end indices
    #a.axis([start_idx, end_idx, min(patient_waveform[start_idx:end_idx]), max(patient_waveform[start_idx:end_idx])])
    a.axis([int(s_idx[s]), int(e_idx[e]), min(patient_waveform[int(s_idx[s]):int(e_idx[e])]), max(patient_waveform[int(s_idx[s]):int(e_idx[e])])])
    a.plot(patient_waveform, color='blue')
    #a.plot(patient_waveform[int(start_idx):int(end_idx)], color='blue')
    #a.plot(patient_waveform[0:239], color='blue')
    #a.plot(patient_pulse_data.data_final, color='blue')
    plot_title = patient_name.get() + " Waveform"
    a.set_title(plot_title, fontsize=14)
    a.set_ylabel("Y", fontsize=14)
    a.set_xlabel("X", fontsize=14)
    # Update/Draw new waveform --> canvas
    canvas.draw()

def show_plot_button_func():
    show_plot_button.config(state='disabled')
    refresh_plot()

def zoom_button_func():
    global plot_zoomed, patient_pulse_data, patient_waveform, start_idx, end_idx, s, e
    # Plot is zoomed in
    if plot_zoomed:
        print "Zooming out..."
        # Show full plot
        #patient_waveform = patient_pulse_data.data_final
        start_idx = 0
        end_idx = len(patient_pulse_data.data_final)
        # Disable Zoom Out button
        zoom_out_button.config(state='disabled')
        # Enable Zoom In button
        zoom_in_button.config(state='active')
        # Disable Move Right/Left buttons
        move_right_button.config(state='disabled')
        move_left_button.config(state='disabled')
        plot_zoomed = 0
        s = 0
        e = 4
        refresh_plot()
    else:
        print "Zooming in..."
        # Zoom into first 1/5 of the waveform
        start_idx = 0
        n = len(patient_pulse_data.data_final)
        end_idx = int(round(n/5))
        print end_idx
        #patient_waveform = patient_pulse_data.data_final[start_idx:end_idx]
        # Enable Zoom Out button
        zoom_out_button.config(state='active')
        # Disable Zoom In button
        zoom_in_button.config(state='disabled')
        # Enable Move Right button
        move_right_button.config(state='active')
        plot_zoomed = 1
        s = 0
        e = 0
        refresh_plot()

def move_right_button_func():
    global s, e
    # If move_right_button is clicked, move_left will always be an option
    move_left_button.config(state='active')
    # Reached end of graph
    if s >= 4 or e >=4:
        move_right_button.config(state='disabled')
    else:
        s += 1
        e += 1
    refresh_plot()

def move_left_button_func():
    global s, e
    # If move_left_button is clicked, move_right will always be an option
    move_right_button.config(state='active')
    # Reached start of graph
    if s <= 0 or e <= 0:
        move_left_button.config(state='disabled')
    else:
        s -= 1
        e -= 1
    refresh_plot()

def load_plot_button_func():
    global patient_pulse_data, fm, patient_waveform
    print "Attempting to load patient data..."
    load_plot_button.config(state='disabled')
    patient_pulse_data = fm.load_all_data(load_plot_var.get())
    print patient_pulse_data.bpm
    patient_waveform = patient_pulse_data.data_final
    refresh_plot()
def save_patient_data_button_func():
    global patient_waveform, fm
    print "Attempting to save patient data..."
    save_patient_data_button.config(state='disabled')
    #file_manager.save(save_filename.get(), patient_waveform)  -- or something like this
    fm.save_all_data(save_filename.get(), patient_pulse_data)


## END Abling functions


### Left frame
#   contains patient info + measurement frames
# Constants
left_frame_width = 400
left_frame_height = window_height
# END Constants
#left_frame = Frame(window, width=left_frame_width, height=left_frame_height)
left_frame = Frame(window, background='#bcd6ff')
left_frame.pack(side=LEFT, expand=False)
#left_frame.place(width=left_frame_width, height=left_frame_height)

## Information frame
info_frame = Frame(left_frame, width=left_frame_width, height=left_frame_height/2)
info_frame.pack(side=TOP, expand=False)
# For patient information (name)
patient_info_frame = Frame(info_frame)
patient_info_frame.pack(side=TOP)
# For test/measurement information (sampling period)
measure_info_frame = Frame(info_frame)
measure_info_frame.pack(side=BOTTOM)

# 'Enter Patient Name' Entry (textbox)
patient_name = StringVar()
#patient_name.trace("w", patient_name_func())
patient_name_entry = Entry(patient_info_frame, textvariable=patient_name)
patient_name_entry.insert(0, "Enter Patient Name")
patient_name_entry.pack(side=LEFT)
# 'Enter Patient Name' Submit button (confirm name)
submit_name_button = Button(patient_info_frame, text="SUBMIT", command=submit_name_button_func)
submit_name_button.pack(side=RIGHT)

# 'Enter Sample Period' Entry (textbox)
sample_period = IntVar()
sample_period_entry = Entry(measure_info_frame, textvariable=sample_period)
sample_period_entry.pack(side=LEFT)
# 'Enter Sample Period' Submit button
submit_measure_button = Button(measure_info_frame, text="SUBMIT", command=submit_measure_button_func)
submit_measure_button.pack(side=RIGHT)

## Test & Measurement frame
measurement_frame = Frame(left_frame, width=left_frame_width, height=left_frame_height/2)
measurement_frame.pack(side=BOTTOM, expand=False)
# 'Start Measurement' Button
start_measure_button = Button(measurement_frame, text="Start Measurement", command=start_measure_button_func)
start_measure_button.pack(side=TOP)
# Progress Bar                                  TO BE IMPLEMENTED
progressbar_canvas = Canvas(measurement_frame, width=200, height=50)
progressbar_canvas.pack(side=BOTTOM)
progressbar = progressbar_canvas.create_rectangle(0,0,200,50,fill='white')
#measure_progressbar = Progressbar(measurement_frame, orient="horizontal",length=200,mode="determinate")

### END Left frame

### Right frame
#   contains plot frame
# Constants
right_frame_width = window_width-left_frame_width
right_frame_height = window_height
# END Constants
right_frame = Frame(window, width=right_frame_width, height=right_frame_height, background='#f7ffd3')
right_frame.pack(side=RIGHT, expand=False)
#right_frame.place(relx=0.5,rely=0.5,anchor=CENTER)
# Waveform plot frame
waveform_frame = Frame(right_frame)
waveform_frame.pack(side=TOP)

# 'Plot Option' buttons
plot_option_frame = Frame(waveform_frame)
plot_option_frame.pack(side=RIGHT)
show_plot_button = Button(plot_option_frame, text="Show Plot", command=show_plot_button_func)
show_plot_button.config(state='disabled')
show_plot_button.pack(side=TOP)

# 'Load Plot' button                     [FUNCTIONALITY] -->         TO BE IMPLEMENTED
load_plot_var = StringVar(plot_option_frame)
load_plot_var.set("None")   # default value - no patient
#load_plot_option = OptionMenu(plot_option_frame, load_plot_var, *fm.patient_dir_names, command=load_plot_button_func)

load_plot_option = OptionMenu(plot_option_frame, load_plot_var, *fm.patient_dir_names)
#load_plot_option.config(command=load_plot_button_func)


load_plot_option.pack(side=BOTTOM)
load_plot_button = Button(plot_option_frame, text="Load", command=load_plot_button_func)
load_plot_button.pack(side=BOTTOM)
load_plot_button.config(state='disabled')


## Plot Navigation Buttons
# 'Zoom In/Out' buttons
zoom_in_button = Button(plot_option_frame, text="Zoom In", command=zoom_button_func)
zoom_in_button.pack(side=TOP)
zoom_in_button.config(state='disabled')
zoom_out_button = Button(plot_option_frame, text="Zoom Out", command=zoom_button_func)
zoom_out_button.pack(side=TOP)
zoom_out_button.config(state='disabled')
# 'Move Right/Left' buttons
move_right_button = Button(plot_option_frame, text=">>>", command=move_right_button_func)
move_right_button.pack(side=TOP)
move_right_button.config(state='disabled')
move_left_button = Button(plot_option_frame, text="<<<", command=move_left_button_func)
move_left_button.pack(side=TOP)
move_left_button.config(state='disabled')

# Initialize Waveform Plot w/ zero-valued data
plot_figure = Figure(figsize=(6,6))
a = plot_figure.add_subplot(111)
a.plot(patient_waveform, color='blue')
plot_title = patient_name.get() + " Waveform"
a.set_title(plot_title, fontsize=14)
a.set_ylabel("Y", fontsize=14)
a.set_xlabel("X", fontsize=14)
canvas = FigureCanvasTkAgg(plot_figure, master=waveform_frame)
canvas.get_tk_widget().pack(side=TOP)
canvas.draw()

# Pulse Analysis Information frame
#   contains: BPM, filename
analysis_info_frame = Frame(right_frame)
analysis_info_frame.pack(side=BOTTOM)
# BPM Label
bpm_frame = Frame(analysis_info_frame)
bpm_frame.pack(side=TOP)
bpm_text_label = Label(bpm_frame, text="Beats Per Minute (BPM): ")
bpm_text_label.pack(side=LEFT)
# No BPM value before test is finished
bpm_value_label = Label(bpm_frame, text="-")
bpm_value_label.pack(side=RIGHT)

# 'Save Patient Data' frame
save_patient_data_frame = Frame(analysis_info_frame)
save_patient_data_frame.pack(side=BOTTOM)
# 'Save Patient Data' button
save_patient_data_button = Button(save_patient_data_frame, text="Save", command=save_patient_data_button_func)
save_patient_data_button.pack(side=LEFT)
# '.txt' label
save_patient_data_label = Label(save_patient_data_frame, text=".txt")
save_patient_data_label.pack(side=RIGHT)
# 'Enter filename' entry
save_filename = StringVar()
save_patient_data_entry = Entry(save_patient_data_frame, textvariable=save_filename)
save_patient_data_entry.insert(0, patient_name.get().replace(" ", "_"))
save_patient_data_entry.pack()

### END Right frame





window.mainloop()
