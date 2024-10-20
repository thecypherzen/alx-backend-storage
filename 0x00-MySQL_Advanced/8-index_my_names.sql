-- Creates an index `idx_name_first` on the table `names` and the first letter of `name`.
-- Requirements:
--   (1). Only first letter of `name` must be indexed.

-- the index
CREATE INDEX idx_name_first ON
names(name(1));
