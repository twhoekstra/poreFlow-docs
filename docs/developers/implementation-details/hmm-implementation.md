# HMM Implementation

## Core Algorithm

Viterbi-based Hidden Markov Model for Hel308 helicase sequencing.

*   **States**: 8192 total. 4096 6-mers $\times$ 2 half-steps (pre/post).
*   **Goal**: Find the most likely sequence of states given observed current levels.

## 1. Emission Model (`smatrixACpar.m`)

Calculates the log-likelihood score $S$ (Gaussian overlap integral) between the observed signal $x_1$ and the model state $x_2$.

$$
S = -0.5 d \ln(2\pi) + 0.5(\ln|\Lambda_1| + \ln|\Lambda_2| - \ln|\Lambda_1+\Lambda_2| - R)
$$

Where:

*   $R = x_1^T\Lambda_1x_1 + x_2^T\Lambda_2x_2 - (\Lambda_1x_1+\Lambda_2x_2)^T(\Lambda_1+\Lambda_2)^{-1}(\Lambda_1x_1+\Lambda_2x_2)$
*   $\Lambda = \Sigma^{-1}$ (Precision/Stiffness matrix)

**Implementation Note**: Use Cholesky decomposition for stable log-determinant calculation.

## 2. Transition Model (`calculateSequenceVV.m`)

Transitions are defined by the data in `transition_info_hel308_6mer.npz` (originally from `transition_info_hel308_6mer.mat`).

*   **Logic**: `p_vals` = `p_combos` $\otimes$ `perms_matrix` (Tensor contraction).
*   **Topology**: Defines valid moves between half-steps and kmers.

**Transition Parameters:**

The transition logic relies on three key matrices found in `transition_info_hel308_6mer.npz`:

*   **p_combos**: A matrix of probability weights. Columns likely correspond to different transition types (e.g., back-step, stay, forward-1-step, etc.). It defines the prior probability of a specific type of move occurring.
*   **perms_matrix**: A large matrix (approx. 8192x8192 implied by file size) mapping state pairs to their specific transition type index. It acts as a lookup table to determine which column of `p_combos` applies to a transition from State A to State B.
*   **step_size_matrix**: A matrix of the same dimensions as `perms_matrix`, defining the physical distance (in half-steps) for each transition. This is used to track the "net movement" along the DNA strand.

## 3. Viterbi Forward Pass

Iterates through signal levels ($t=1..T$).

*   **Handling Bad Levels**: Allows skipping up to $B$ bad measurements.
*   **Pruning**: States with score < `max_score - cutoff` are dropped to optimize speed.
*   **Matrices**:
    *   `score_matrix`: Best score for state $i$ at time $t$.
    *   `traceback_matrix`: Predecessor index for the best path.

## 4. Traceback & Parity

Reconstructs the path from end to start.

*   **Parity Constraint**: Enforces physical consistency of Hel308 half-steps. The helicase moves in discrete half-steps, so the path must alternate logical "even" and "odd" states (or maintain parity depending on the step size).
*   **Final Output**: Consolidates the sequence of half-steps into a final nucleotide sequence.

## Asset Mapping

*   `pore_model_6mer_constant_voltage.csv` $\rightarrow$ **Emission Params** (Means $\mu$, Stiffness $\Lambda$).
*   `transition_info_hel308_6mer.npz` $\rightarrow$ **Transition Params** (`p_combos`, `perms_matrix`, `step_size`).
