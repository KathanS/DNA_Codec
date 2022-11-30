% Setup code parameters

function [output_decoded_bits]=decodePolar(encoded_bits)
    secret_code = fileread('decode_code.txt');
    fileName = append(secret_code, ".mat");
    load(fileName)
    len = size(f,2);
    encoded_len = size(encoded_bits,2);
    for i=1:encoded_len/len
        disp(i);
        % Decode and compute error rate for info bits
        y = encoded_bits(:,(len*(i-1)+1):(len*i));
        [uhat,xhat] = polar_decode(y,f);
        output_decoded_bits(:,(k*(i-1)+1):(k*i)) = uhat(A);
        %biterr(i) = mean(uhat(A)~=u(A));
    end
end