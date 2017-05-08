function [] = waver(filename)

% load .txt file of provided 'filename'
% file should list data vertically, with a new 
% line separating every data point
x = load(filename);

% clean up signals from NaN values and outliers
idx = find(isnan(x));
x(idx) = [];
x = x(x > 1000);
x = x(x < 10000);

% reduce noise w/ moving average filter
%signal data after being filtered once
smx0 = smooth(x);
%signal data after being filtered twice
smx1 = smooth(smx0);
%any further noise reduction would result in loss
%of signal data

% adjust for baseline wander w/ difference method
%original signal data w/ noise
xd = diff(x);
fx = smooth(xd);
%signal data w/ some noise
xd0 = diff(smx0);
fx0 = smooth(xd0);
%signal data w/ least amount of noise
xd1 = diff(smx1);
fx1 = smooth(xd1);

% Display the results
figure(1)
%This data range allows for users to better see 
%their pulse waveforms
title('Data Range [0, 10] seconds')
plot(1:200,fx(1:200),'y',1:200,fx0(1:200),'c',1:200,fx1(1:200),'b')
legend('fx','fx0','fx1')

figure(2)
%This data is the full minute-long waveform
title('Full Data Range [0, 60] seconds')
plot(1:length(fx),fx,'y',1:length(fx0),fx0,'c',1:length(fx1),fx1,'b')
legend('fx','fx0','fx1')

% Each pulse has a peak in which the measured
% light is highest- this represents the tail 
% end of a pulse, when the blood is leaving
bpm = length(findpeaks(fx1));

fprintf('BPM: %d\n',bpm);

% The final pulse waveform
pulseWaveform = fx1;
end
