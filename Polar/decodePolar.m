% Setup code parameters

function [output_decoded_bits]=decodePolar(encoded_bits)
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
    len = size(f,2);
    encoded_len = size(encoded_bits,2);
    for i=1:encoded_len/len
        % Decode and compute error rate for info bits
        y = encoded_bits(:,(len*(i-1)+1):(len*i));
        [uhat,xhat] = polar_decode(y,f);
        output_decoded_bits(:,(k*(i-1)+1):(k*i)) = uhat(A);
        biterr(i) = mean(uhat(A)~=u(A));
    end