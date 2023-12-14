function [mat,exc] = asWindow_New(mat,exc, Time,WindowSize = 100)
% the function cuts the time seires in pieces of timelegth windowSize and
% returns small pieces with an overlap 
     
    overlap = 0.5;
    if WindowSize ~= none
        nWindows = int(round(Time(end) - Time(1)) / WindowSize / (1-overlap));
        for i=1:size(nWindows,1)
            Fr = 1/(Time(end) - Time(1)); 
            tRange = Time(1) + i*windowSize*(1 - overlap) + (0:1:WindowSize); 
            Elements = round(tRange*Fr); 
            mat_small = mat(Elements(1:2)); 
            exc_small = exc(Elements(1:2));
        end 
    else 
        mat = mat; exc = exc; 
    end  
end