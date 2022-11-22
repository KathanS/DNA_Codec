% Setup code parameters

function [f,A,k]=setupPolar()
    n = 12; N = 2^n;
    e = 0.1; p = 0.1;
    d = 0.5; bec = 0; % as you increase d rate increases! but also rate of error, although for no channel error rate = 0 always!
    
    % Compute the quality of all effective channels
    if (bec)
        [biterrd] = polar_bec(n,e);
    else
        [biterrd] = polar_bsc(n,p,1000);
    end
    
    % Design polar code
    f = polar_design(biterrd,d);
    A = (f==1/2);
    k = sum(A);
    rate = k/N;
end