#include <stdio.h>
#include <stdlib.h>
#include <curl/curl.h>

// Callback function to write data to a file
size_t WriteCallback(void* ptr, size_t size, size_t nmemb, FILE* stream) {
    return fwrite(ptr, size, nmemb, stream);
}

void download_file(const char* url, const char* output_file) {
    CURL* curl;
    CURLcode res;

    // Initialize CURL
    curl = curl_easy_init();
    if (curl) {
        // Open file for writing in binary mode
        FILE* file = fopen(output_file, "wb");
        if (!file) {
            fprintf(stderr, "Failed to open file for writing: %s\n", output_file);
            return;
        }

        // Set the URL
        curl_easy_setopt(curl, CURLOPT_URL, url);

        // Set the callback function to write the downloaded data
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);

        // Pass the file pointer as the user data to the callback
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, file);

        // Perform the request
        res = curl_easy_perform(curl);

        // Check if the request was successful
        if (res != CURLE_OK) {
            fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(res));
        } else {
            printf("File downloaded successfully: %s\n", output_file);
        }

        // Cleanup
        fclose(file);
        curl_easy_cleanup(curl);
    } else {
        fprintf(stderr, "Failed to initialize CURL\n");
    }
}

int main() {
    // Example usage
    const char* url = "https://ftp.gnu.org/gnu/wget/wget-latest.tar.gz";
    const char* output_file = "wget-latest.tar.gz";

    download_file(url, output_file);

    return 0;
}
