% Setup code parameters

function [output_encoded_bits]=encodePolar(input_bits,f,A,k)
    input_length = size(input_bits,2);
    
    if (mod(input_length,k) ~= 0)
        input_bits = [input_bits,zeros(1,k - mod(input_length,k))];
        input_length = size(input_bits,2);
    end
    for i=1:input_length/k
        % Set frozen bits, add random data, and encode
        u = f;
        %u(A) = rand(1,k)<0.5; % input, k is number of input bits, thus when we have input bits pass it in packets of size k. % Packets size is also needed while decoding!
        u(A) = input_bits(:,(k*(i-1)+1):(k*i));
        x = polar_transform(u);
    
        y = x; % no channel
        output_encoded_bits=x;
    end
end