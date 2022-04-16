#include <stdio.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

char *Dync_size(int size);

char *Dync_size(int size) {
    char *str = (char *)malloc(sizeof(char)*size);

    return str;
}

unsigned char pack( char *str ) {
    unsigned char result = 0;
    cout << "start. " <<str << endl;
    for (int i = 7; i >= 0; i--) {
        if ( *str == '1' ) {
            result = result | ( 1 << i );
        }
        str++;
        cout << str << endl;
    }
    return result;
}

string binary_to_string(string path) {
    unsigned char c;
    int mask, res;
    string str;
    ifstream input(path, ios::in | ios::binary);

    while(true) {
        input.read((char*)&c, sizeof(unsigned char));
        if(input.eof()){
            break;
        }
        for(int i = 7;i>=0;i--){
            mask = 1 << i;
            res = c & mask ? 1:0;
            str.append(to_string(res));
        }
    }
    input.close();
    return str;
}

void string_to_binary(string str, string output_filename) {
    // 기록할 시퀀스
    // char buf[40] = "010000010100001001000011010";  // 27자
    char *buf = Dync_size(str.length());
    strcpy(buf, str.c_str()); 
    // 시퀀스의 원래 길이
    int str_len = strlen( buf );                        // 27
    // 8의 배수로 맞추기 위해서 몇을 더해야 하나?
    int padding_len = ( 8 - ( str_len % 8 ) ) % 8;      // 5
    // 필요한 만큼 '0'을 추가
    for (int i=0; i<padding_len; i++) {
        strcat(buf, "0");
    }
    // 파일에 기록
    FILE * fp = fopen(output_filename.c_str(), "wb");
    char * buf_ptr = buf;   // 첫 글자를 가리키게 하고
    for (int i=0; i*8 < strlen(buf); i++) {
        // buf_ptr이 가리키는 곳부터 8바이트를 unsigned char 한 바이트로 압축
        unsigned char byte = pack( buf_ptr );
        // 파일에 기록
        fputc( byte, fp );
        // 그 뒤의 8바이트를 읽기 위해 이동
        buf_ptr += 8;
    }
    fclose(fp);
    free(buf);
}

int main() {
    string bin;
    string_to_binary("11110000", "output.bin");
    bin = binary_to_string("output.bin");
    cout << bin;
}