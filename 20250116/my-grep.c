#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <sys/stat.h>
#include <errno.h>

/**
 * Recursively search a directory (dirPath) for files/directories
 * whose NAME contains the given pattern.
 * Prints the full path of any matching entry.
 */
void searchDirectory(const char *dirPath, const char *pattern);

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        fprintf(stderr, "Usage: %s <pattern> [start-directory]\n", argv[0]);
        return 1;
    }

    const char *pattern = argv[1];
    const char *startDir = (argc > 2) ? argv[2] : ".";  // default to current dir

    searchDirectory(startDir, pattern);
    return 0;
}

void searchDirectory(const char *dirPath, const char *pattern)
{
    DIR *dir = opendir(dirPath);
    if (!dir)
    {
        fprintf(stderr, "Could not open directory '%s': %s\n", dirPath, strerror(errno));
        return;
    }

    struct dirent *entry;
    while ((entry = readdir(dir)) != NULL)
    {
        // Skip "." and ".." to avoid infinite recursion
        if (strcmp(entry->d_name, ".") == 0 || strcmp(entry->d_name, "..") == 0)
            continue;

        // Build full path: dirPath + "/" + entry->d_name
        char pathBuf[1024];
        snprintf(pathBuf, sizeof(pathBuf), "%s/%s", dirPath, entry->d_name);

        // Does the NAME contain the pattern?
        if (strstr(entry->d_name, pattern) != NULL)
        {
            printf("%s\n", pathBuf);
        }

        // Check if it's a directory, then recurse
        struct stat st;
        if (stat(pathBuf, &st) == 0 && S_ISDIR(st.st_mode))
        {
            // Recursively search subdirectory
            searchDirectory(pathBuf, pattern);
        }
    }

    closedir(dir);
}
