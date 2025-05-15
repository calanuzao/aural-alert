classdef SimuSpatialCuesPlugin < audioPlugin
    methods
        function out = process(plugin, in)
            % Assume stereo input: in(:,1) = left, in(:,2) = right
            [ILD, ITD, Xcorr, CLL, freqs] = simuspatcues(in(:,1), in(:,2), getSampleRate(plugin));
            % For a VST, you typically process and return audio.
            % Here, just pass audio through (bypass), or process as needed.
            out = in;
            % You can also expose ILD, ITD, etc., as plugin parameters or outputs.
        end
    end
end
