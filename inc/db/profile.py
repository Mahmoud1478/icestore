class QueryProfile:
    pass

    def _query_profiling(self, query: str, values: tuple = None):
        start = time.time()
        self.__cursor.execute(str(query), values)
        print(f"{self.__cursor._executed}  {time.time() - start : .4f}s")
        return self
