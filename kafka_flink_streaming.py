from pyflink.table import TableEnvironment, EnvironmentSettings

# Create a TableEnvironment
env_settings = EnvironmentSettings.in_streaming_mode()
t_env = TableEnvironment.create(env_settings)

# Specify connector and format jars
t_env.get_config().get_configuration().set_string(
    "pipeline.jars",
    "file:/home/laadaili/flink/lib/flink-sql-connector-kafka-3.0.2-1.18.jar"
)


#/home/amine/Downloads/flink-sql-connector-kafka_2.11-1.14.4.jar
# Define source table DDL
source_ddl = """
    CREATE TABLE source_table(
                    description VARCHAR,
                    title VARCHAR,
                    url VARCHAR,
                    author VARCHAR,
                    publishedAt VARCHAR,
                    content VARCHAR,
                    source_id VARCHAR,
                    source_name VARCHAR,
                    urlToImage VARCHAR
    ) WITH (
  'connector' = 'kafka',
        'topic' = 'topic_aya',
        'properties.bootstrap.servers' = 'localhost:9092',
        'properties.group.id' = 'test_3',
        'scan.startup.mode' = 'latest-offset',
        'format' = 'json'
    )
"""

# Execute DDL statement to create the source table
t_env.execute_sql(source_ddl)

# Retrieve the source table
source_table = t_env.from_path('source_table')

print("Source Table Schema:")
source_table.print_schema()

# Define a SQL query to select all columns from the source table
sql_query = "SELECT * FROM source_table"

# Execute the query and retrieve the result table
result_table = t_env.sql_query(sql_query)

# Print the result table to the console
result_table.execute().print()

