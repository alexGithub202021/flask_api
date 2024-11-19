from datetime import datetime as dt
import json

class Functions:

    def convert_to_json(self, cursor):
        results = cursor.fetchall()
        rows = []
        for row in results:
            row_dict = {}
            for idx, value in enumerate(row):
                if isinstance(value, dt):
                    row_dict[cursor.column_names[idx]] = value.strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )
                else:
                    row_dict[cursor.column_names[idx]] = value
            rows.append(row_dict)

        # Serialize the list of dictionaries to JSON format
        json_output = json.loads(json.dumps(rows))
        return json_output

    def parse_datetime(self, input_datetime):
        # Parse input date string
        parsed_date = dt.strptime(input_datetime, "%d/%m/%Y")
        current_time = dt.now().time()
        combined_datetime = dt.combine(parsed_date, current_time)
        output_datetime = combined_datetime.strftime("%Y-%m-%d %H:%M:%S")
        return output_datetime
