class FakeCategoryRepository:
    records = []

    def add_category(self, category_name, description):
        self.records.append({
            'category_name': category_name,
            'description': description
        })

    def get_category_by_name(self, category_name):
        for record in self.records:
            if record['category_name'] == category_name:
                return record
