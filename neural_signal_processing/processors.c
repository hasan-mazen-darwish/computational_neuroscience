#include <stddef.h>
#include <stdlib.h>

// This function will take the signals, and return an array (or a list in
// Python) that averages these signals. We will take the signals as 0/1, and
// return them as doubles.
// The window is the number of spikes that will get averaged together (that they
// will be added together and then get divided), and the size attribute that
// maps the size of the data (number of spikes.
double *average_spikes(int *data, unsigned int window, size_t size) {
  double *result = malloc(size * sizeof(double));
  double avg = 0.0;
  if (result == NULL)
    return NULL;

  int i = 0;
  for (i = 0; i < size; i += window) {
    if (i >= size) {
      i -= window;
      break;
    }

    avg = 0.0;
    for (int j = 0; j < window; j++)
      avg += data[i + j];
    avg /= window;
    for (int j = 0; j < window; j++)
      result[i + j] = avg;
  }

  // One final loop for the elements that were not included in the last
  // iteration:
  int new_window = size - i;
  avg = 0.0;
  int j = 0;
  while (j < new_window) {
    if (i + j == size)
      break;
    avg += data[i + j];
    j++;
  }
  avg /= new_window;

  return result;
}

// A function used for freeing any allocation result after finishing
void free_pointer(void *pointer) {
  free(pointer);
  return;
}
