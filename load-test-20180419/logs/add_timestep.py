import csv


current_name = None
line_count = 0

with open('results.csv', 'w') as outfile:
    csvWriter = csv.writer(outfile)
    csvWriter.writerow(['time_step', 'test_name', 'docker_cpu_pct'])

    with open('results_raw.csv') as infile:
         csvReader = csv.reader(infile)
         csvReader.next()

         for row in csvReader:
             in_name = row[0]

             if in_name != current_name:
                 print 'found new name {}'.format(in_name)
                 line_count = 0
                 current_name = in_name

             line_count += 1
             csvWriter.writerow([line_count] + row)
