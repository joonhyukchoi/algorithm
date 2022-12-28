template <RandomAccessIterator I, Integer N>
void sift(I first, N n) {
  I last = first + n;
  std::fill(first, last, true);
  N i(0);
  N index_square(3);
  N factor(3);
  while (index_square < n) {
    if (first[i]) {
      mark_sieve(first + index_square, last, factor);
    }
    ++i;
    index_square += factor;
    factor += N(2);
    index_square += factor;
  }
}
