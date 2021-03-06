import cgi
import model
import view
import os

PIVOT = 'select.html'
CONTROLLER = 'controller.py'
SEARCH_ERROR = 'No item was found'

def main():
        
    
    prev_addr = os.getenv('HTTP_REFERER')
    prev_page = None
    if prev_addr != None:
        prev_page = prev_addr.split('/')[-1]

    if prev_page == PIVOT:
    
        form = cgi.FieldStorage()

        # get values sent via form

        row = form.getvalue('row')
        col = form.getvalue('col')
        val = form.getvalue('val')
        mode = form.getvalue('mode')
        searchby = form.getvalue('searchby')
        search = form.getvalue('search')

        try:

            all_data = model.get_all_data(model.DATA_FILE)
            interval = model.att_intervals()

            # get key elements from row and column

            if row in ['Season', 'Tm']:
                #get unique values for row 
                unique_row = model.create_keys(all_data, row)
                #row header for table str 
                unique_row_str = unique_row
            else:
                #find the min and max value for row
                row_min_max = model.min_max(all_data, row)
                #row header
                unique_row = model.get_bin_header(row_min_max[0],row_min_max[1], interval[row])
                #row header for table str
                unique_row_str = model.get_bin_str(unique_row)

            if col in ['Season', 'Tm']:
                #get unique values for col
                unique_col = model.create_keys(all_data, col)
                #row header for table col
                unique_col_str = unique_col
            else:
                #find the min and max value for col
                col_min_max = model.min_max(all_data, col)
                #col header
                unique_col = model.get_bin_header(col_min_max[0],col_min_max[1], interval[col])
                #col header for table str 
                unique_col_str = model.get_bin_str(unique_col)

            # if search query is passed, filter unique_row or unique_col using the query
            search_row = row
            search_col = col
            if searchby and search:
                
                if row == searchby:
                    temp = [item for item in unique_row if item == search]
                    if temp != []:
                        unique_row = temp
                        unique_row_str = temp
                    else:
                        #item not in csv file
                        raise ValueError(SEARCH_ERROR)
                elif col == searchby:

                    temp = [item for item in unique_col if item == search]

                    if temp != []:
                        unique_col = temp
                        unique_col_str = temp
                    else:
                        raise ValueError(SEARCH_ERROR)

                


            # get pivot table values
            pvt_vals = model.get_pvt_vals(
                all_data,
                row,
                col,
                val,
                mode,
                unique_row,
                unique_col,
                )

            # add sum of rows and columns to pvt_vals
            pvt_vals = model.pvt_table_total(pvt_vals)

            # add total to the end of row header and column header
            unique_row_str.append('Total')
            unique_col_str.append('Total')
            
            # get pivot table title
            title_str = view.create_title(row, col, val, mode, searchby, search)
            
            # get html of the pivot table contents
            html_str = view.create_table_str(pvt_vals, unique_row_str)

            # print html_str
            if html_str:
                view.print_table(pvt_vals, title_str,row, unique_row_str, unique_col_str, html_str)
                
        except ValueError, val_err:

            view.print_error(val_err)
            
    elif prev_page == CONTROLLER:
        
        view.print_select()
        
    else:

        view.print_home()

main()
        

