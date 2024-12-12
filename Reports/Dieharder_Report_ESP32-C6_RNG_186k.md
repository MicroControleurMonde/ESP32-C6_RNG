# Dieharder Test Results

1. **Test Results**:
   - **All tests pass** (except one), which suggests that the generated numbers are of high quality and well-distributed.
   - **Diehard tests**: The majority of Diehard tests (such as `diehard_birthdays`, `diehard_operm5`, `diehard_rank_32x32`, etc.) passed with good p-values (generally well above the critical threshold of 0.01), indicating that the data follows expected statistical distributions for random numbers.
   - **`sts_serial` test**: There is one notable exception with the **`sts_serial` for the 8th bit** (ntuple = 8), where the p-value is **0.9991**, which is **classified as "WEAK"**. This could indicate a small bias in this bit sequence, but it does not necessarily mean that the overall quality of the RNG is poor.
     - Other tests like **`rgb_lagged_sum`** and **`rgb_bitdist`** show no detected weaknesses.

2. **Conclusion**:
   - **"PASSED" for almost all tests**: This shows that the random number generator (RNG) produces reliable and well-distributed results for the majority of statistical tests.
   - **"WEAK" for one specific test (`sts_serial` ntuple 8)**: Although this is a deviation, it does not undermine the overall validity of the results, and most of the other tests showed no issues.
