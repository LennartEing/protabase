from pandas import read_excel


class ExcelLoader:

    def __init__(self, path):
        self._path = path

    def set_path(self, path):
        self._path = path

    def load(self):
        return CompoundData(read_excel(self._path))


class CompoundData:

    def __init__(self, df):
        self._df = df
        self._column_labeling = self.set_columns_labeling()
        self._number_of_compounds = self.set_number_of_compounds()
        self._concentration_column = self.set_concentration_column()
        self._concentration_lower_index_bound, self._concentration_upper_index_bound = \
            self.set_concentration_idx_bounds()
        self._level_columns = self.set_level_columns()
        self._sd_columns = self.set_sd_columns()
        self._level_lower_index_bound, self._level_upper_index_bound = self.set_level_idx_bounds()
        self._sd_lower_index_bound, self._sd_upper_index_bound = self.set_sd_idx_bounds()

    def set_number_of_compounds(self, number=4):
        self._number_of_compounds = number
        return self._number_of_compounds

    def set_columns_labeling(self,
                             labeling=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                                       'o', 'p', 'q', 'r', 's', 't', 'u', 'v']
                             ):
        self._column_labeling = labeling
        self._df.columns = self._column_labeling
        return self._column_labeling

    def set_concentration_column(self, column='q'):
        self._concentration_column = column
        return column

    def set_level_columns(self, compound_0_column='o', columns=None):
        if columns is not None:
            self._level_columns = columns
        elif compound_0_column is not None:
            self._level_columns = [chr(ord(compound_0_column) + compound_number * 2)
                                   for compound_number in range(self._number_of_compounds)]
        return self._level_columns

    def set_sd_columns(self, compound_0_column='p', columns=None):
        if columns is not None:
            self._sd_columns = columns
        elif compound_0_column is not None:
            self._sd_columns = [chr(ord(compound_0_column) + compound_number * 2)
                                for compound_number in range(self._number_of_compounds)]
        return self._sd_columns

    def set_concentration_idx_bounds(self, lower_bound=10, upper_bound=18):
        self._concentration_lower_index_bound = lower_bound
        self._concentration_upper_index_bound = upper_bound
        return lower_bound, upper_bound

    def set_level_idx_bounds(self, lower_bound=26, upper_bound=34, bounds=None):
        if bounds is not None:
            self._level_lower_index_bound, self._level_upper_index_bound = bounds
        elif lower_bound is not None and upper_bound is not None:
            self._level_lower_index_bound = [lower_bound for _ in range(self._number_of_compounds)]
            self._level_upper_index_bound = [upper_bound for _ in range(self._number_of_compounds)]
        return self._level_lower_index_bound, self._level_upper_index_bound

    def set_sd_idx_bounds(self, lower_bound=26, upper_bound=34, bounds=None):
        if bounds is not None:
            self._sd_lower_index_bound, self._sd_upper_index_bound = bounds
        elif lower_bound is not None and upper_bound is not None:
            self._sd_lower_index_bound = [lower_bound for _ in range(self._number_of_compounds)]
            self._sd_upper_index_bound = [upper_bound for _ in range(self._number_of_compounds)]
        return self._sd_lower_index_bound, self._sd_upper_index_bound

    def get(self, compound_number):
        concentration = self._df[self._concentration_column][self._concentration_lower_index_bound:
                                                             self._concentration_upper_index_bound] \
            .to_numpy()
        level = self._df[self._level_columns[compound_number]][self._level_lower_index_bound[compound_number]:
                                                               self._level_upper_index_bound[compound_number]] \
            .to_numpy()
        sd = self._df[self._sd_columns[compound_number]][self._sd_lower_index_bound[compound_number]:
                                                         self._sd_upper_index_bound[compound_number]] \
            .to_numpy()
        return concentration, level, sd