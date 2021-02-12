// ORM class for table 'newemployee'
// WARNING: This class is AUTO-GENERATED. Modify at your own risk.
//
// Debug information:
// Generated date: Mon Jan 11 22:30:50 IST 2021
// For connector: org.apache.sqoop.manager.MySQLManager
import org.apache.hadoop.io.BytesWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.io.Writable;
import org.apache.hadoop.mapred.lib.db.DBWritable;
import com.cloudera.sqoop.lib.JdbcWritableBridge;
import com.cloudera.sqoop.lib.DelimiterSet;
import com.cloudera.sqoop.lib.FieldFormatter;
import com.cloudera.sqoop.lib.RecordParser;
import com.cloudera.sqoop.lib.BooleanParser;
import com.cloudera.sqoop.lib.BlobRef;
import com.cloudera.sqoop.lib.ClobRef;
import com.cloudera.sqoop.lib.LargeObjectLoader;
import com.cloudera.sqoop.lib.SqoopRecord;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.io.DataInput;
import java.io.DataOutput;
import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.CharBuffer;
import java.sql.Date;
import java.sql.Time;
import java.sql.Timestamp;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.HashMap;

public class newemployee extends SqoopRecord  implements DBWritable, Writable {
  private final int PROTOCOL_VERSION = 3;
  public int getClassFormatVersion() { return PROTOCOL_VERSION; }
  public static interface FieldSetterCommand {    void setField(Object value);  }  protected ResultSet __cur_result_set;
  private Map<String, FieldSetterCommand> setters = new HashMap<String, FieldSetterCommand>();
  private void init0() {
    setters.put("employeeno", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        newemployee.this.employeeno = (java.math.BigDecimal)value;
      }
    });
    setters.put("ename", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        newemployee.this.ename = (String)value;
      }
    });
    setters.put("job", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        newemployee.this.job = (String)value;
      }
    });
    setters.put("hiredate", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        newemployee.this.hiredate = (java.sql.Date)value;
      }
    });
    setters.put("sal", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        newemployee.this.sal = (java.math.BigDecimal)value;
      }
    });
    setters.put("departmentno", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        newemployee.this.departmentno = (java.math.BigDecimal)value;
      }
    });
  }
  public newemployee() {
    init0();
  }
  private java.math.BigDecimal employeeno;
  public java.math.BigDecimal get_employeeno() {
    return employeeno;
  }
  public void set_employeeno(java.math.BigDecimal employeeno) {
    this.employeeno = employeeno;
  }
  public newemployee with_employeeno(java.math.BigDecimal employeeno) {
    this.employeeno = employeeno;
    return this;
  }
  private String ename;
  public String get_ename() {
    return ename;
  }
  public void set_ename(String ename) {
    this.ename = ename;
  }
  public newemployee with_ename(String ename) {
    this.ename = ename;
    return this;
  }
  private String job;
  public String get_job() {
    return job;
  }
  public void set_job(String job) {
    this.job = job;
  }
  public newemployee with_job(String job) {
    this.job = job;
    return this;
  }
  private java.sql.Date hiredate;
  public java.sql.Date get_hiredate() {
    return hiredate;
  }
  public void set_hiredate(java.sql.Date hiredate) {
    this.hiredate = hiredate;
  }
  public newemployee with_hiredate(java.sql.Date hiredate) {
    this.hiredate = hiredate;
    return this;
  }
  private java.math.BigDecimal sal;
  public java.math.BigDecimal get_sal() {
    return sal;
  }
  public void set_sal(java.math.BigDecimal sal) {
    this.sal = sal;
  }
  public newemployee with_sal(java.math.BigDecimal sal) {
    this.sal = sal;
    return this;
  }
  private java.math.BigDecimal departmentno;
  public java.math.BigDecimal get_departmentno() {
    return departmentno;
  }
  public void set_departmentno(java.math.BigDecimal departmentno) {
    this.departmentno = departmentno;
  }
  public newemployee with_departmentno(java.math.BigDecimal departmentno) {
    this.departmentno = departmentno;
    return this;
  }
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (!(o instanceof newemployee)) {
      return false;
    }
    newemployee that = (newemployee) o;
    boolean equal = true;
    equal = equal && (this.employeeno == null ? that.employeeno == null : this.employeeno.equals(that.employeeno));
    equal = equal && (this.ename == null ? that.ename == null : this.ename.equals(that.ename));
    equal = equal && (this.job == null ? that.job == null : this.job.equals(that.job));
    equal = equal && (this.hiredate == null ? that.hiredate == null : this.hiredate.equals(that.hiredate));
    equal = equal && (this.sal == null ? that.sal == null : this.sal.equals(that.sal));
    equal = equal && (this.departmentno == null ? that.departmentno == null : this.departmentno.equals(that.departmentno));
    return equal;
  }
  public boolean equals0(Object o) {
    if (this == o) {
      return true;
    }
    if (!(o instanceof newemployee)) {
      return false;
    }
    newemployee that = (newemployee) o;
    boolean equal = true;
    equal = equal && (this.employeeno == null ? that.employeeno == null : this.employeeno.equals(that.employeeno));
    equal = equal && (this.ename == null ? that.ename == null : this.ename.equals(that.ename));
    equal = equal && (this.job == null ? that.job == null : this.job.equals(that.job));
    equal = equal && (this.hiredate == null ? that.hiredate == null : this.hiredate.equals(that.hiredate));
    equal = equal && (this.sal == null ? that.sal == null : this.sal.equals(that.sal));
    equal = equal && (this.departmentno == null ? that.departmentno == null : this.departmentno.equals(that.departmentno));
    return equal;
  }
  public void readFields(ResultSet __dbResults) throws SQLException {
    this.__cur_result_set = __dbResults;
    this.employeeno = JdbcWritableBridge.readBigDecimal(1, __dbResults);
    this.ename = JdbcWritableBridge.readString(2, __dbResults);
    this.job = JdbcWritableBridge.readString(3, __dbResults);
    this.hiredate = JdbcWritableBridge.readDate(4, __dbResults);
    this.sal = JdbcWritableBridge.readBigDecimal(5, __dbResults);
    this.departmentno = JdbcWritableBridge.readBigDecimal(6, __dbResults);
  }
  public void readFields0(ResultSet __dbResults) throws SQLException {
    this.employeeno = JdbcWritableBridge.readBigDecimal(1, __dbResults);
    this.ename = JdbcWritableBridge.readString(2, __dbResults);
    this.job = JdbcWritableBridge.readString(3, __dbResults);
    this.hiredate = JdbcWritableBridge.readDate(4, __dbResults);
    this.sal = JdbcWritableBridge.readBigDecimal(5, __dbResults);
    this.departmentno = JdbcWritableBridge.readBigDecimal(6, __dbResults);
  }
  public void loadLargeObjects(LargeObjectLoader __loader)
      throws SQLException, IOException, InterruptedException {
  }
  public void loadLargeObjects0(LargeObjectLoader __loader)
      throws SQLException, IOException, InterruptedException {
  }
  public void write(PreparedStatement __dbStmt) throws SQLException {
    write(__dbStmt, 0);
  }

  public int write(PreparedStatement __dbStmt, int __off) throws SQLException {
    JdbcWritableBridge.writeBigDecimal(employeeno, 1 + __off, 3, __dbStmt);
    JdbcWritableBridge.writeString(ename, 2 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(job, 3 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeDate(hiredate, 4 + __off, 91, __dbStmt);
    JdbcWritableBridge.writeBigDecimal(sal, 5 + __off, 3, __dbStmt);
    JdbcWritableBridge.writeBigDecimal(departmentno, 6 + __off, 3, __dbStmt);
    return 6;
  }
  public void write0(PreparedStatement __dbStmt, int __off) throws SQLException {
    JdbcWritableBridge.writeBigDecimal(employeeno, 1 + __off, 3, __dbStmt);
    JdbcWritableBridge.writeString(ename, 2 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(job, 3 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeDate(hiredate, 4 + __off, 91, __dbStmt);
    JdbcWritableBridge.writeBigDecimal(sal, 5 + __off, 3, __dbStmt);
    JdbcWritableBridge.writeBigDecimal(departmentno, 6 + __off, 3, __dbStmt);
  }
  public void readFields(DataInput __dataIn) throws IOException {
this.readFields0(__dataIn);  }
  public void readFields0(DataInput __dataIn) throws IOException {
    if (__dataIn.readBoolean()) { 
        this.employeeno = null;
    } else {
    this.employeeno = com.cloudera.sqoop.lib.BigDecimalSerializer.readFields(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.ename = null;
    } else {
    this.ename = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.job = null;
    } else {
    this.job = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.hiredate = null;
    } else {
    this.hiredate = new Date(__dataIn.readLong());
    }
    if (__dataIn.readBoolean()) { 
        this.sal = null;
    } else {
    this.sal = com.cloudera.sqoop.lib.BigDecimalSerializer.readFields(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.departmentno = null;
    } else {
    this.departmentno = com.cloudera.sqoop.lib.BigDecimalSerializer.readFields(__dataIn);
    }
  }
  public void write(DataOutput __dataOut) throws IOException {
    if (null == this.employeeno) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    com.cloudera.sqoop.lib.BigDecimalSerializer.write(this.employeeno, __dataOut);
    }
    if (null == this.ename) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, ename);
    }
    if (null == this.job) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, job);
    }
    if (null == this.hiredate) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    __dataOut.writeLong(this.hiredate.getTime());
    }
    if (null == this.sal) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    com.cloudera.sqoop.lib.BigDecimalSerializer.write(this.sal, __dataOut);
    }
    if (null == this.departmentno) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    com.cloudera.sqoop.lib.BigDecimalSerializer.write(this.departmentno, __dataOut);
    }
  }
  public void write0(DataOutput __dataOut) throws IOException {
    if (null == this.employeeno) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    com.cloudera.sqoop.lib.BigDecimalSerializer.write(this.employeeno, __dataOut);
    }
    if (null == this.ename) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, ename);
    }
    if (null == this.job) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, job);
    }
    if (null == this.hiredate) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    __dataOut.writeLong(this.hiredate.getTime());
    }
    if (null == this.sal) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    com.cloudera.sqoop.lib.BigDecimalSerializer.write(this.sal, __dataOut);
    }
    if (null == this.departmentno) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    com.cloudera.sqoop.lib.BigDecimalSerializer.write(this.departmentno, __dataOut);
    }
  }
  private static final DelimiterSet __outputDelimiters = new DelimiterSet((char) 44, (char) 10, (char) 0, (char) 0, false);
  public String toString() {
    return toString(__outputDelimiters, true);
  }
  public String toString(DelimiterSet delimiters) {
    return toString(delimiters, true);
  }
  public String toString(boolean useRecordDelim) {
    return toString(__outputDelimiters, useRecordDelim);
  }
  public String toString(DelimiterSet delimiters, boolean useRecordDelim) {
    StringBuilder __sb = new StringBuilder();
    char fieldDelim = delimiters.getFieldsTerminatedBy();
    __sb.append(FieldFormatter.escapeAndEnclose(employeeno==null?"null":employeeno.toPlainString(), delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(ename==null?"null":ename, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(job==null?"null":job, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(hiredate==null?"null":"" + hiredate, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(sal==null?"null":sal.toPlainString(), delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(departmentno==null?"null":departmentno.toPlainString(), delimiters));
    if (useRecordDelim) {
      __sb.append(delimiters.getLinesTerminatedBy());
    }
    return __sb.toString();
  }
  public void toString0(DelimiterSet delimiters, StringBuilder __sb, char fieldDelim) {
    __sb.append(FieldFormatter.escapeAndEnclose(employeeno==null?"null":employeeno.toPlainString(), delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(ename==null?"null":ename, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(job==null?"null":job, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(hiredate==null?"null":"" + hiredate, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(sal==null?"null":sal.toPlainString(), delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(departmentno==null?"null":departmentno.toPlainString(), delimiters));
  }
  private static final DelimiterSet __inputDelimiters = new DelimiterSet((char) 44, (char) 10, (char) 0, (char) 0, false);
  private RecordParser __parser;
  public void parse(Text __record) throws RecordParser.ParseError {
    if (null == this.__parser) {
      this.__parser = new RecordParser(__inputDelimiters);
    }
    List<String> __fields = this.__parser.parseRecord(__record);
    __loadFromFields(__fields);
  }

  public void parse(CharSequence __record) throws RecordParser.ParseError {
    if (null == this.__parser) {
      this.__parser = new RecordParser(__inputDelimiters);
    }
    List<String> __fields = this.__parser.parseRecord(__record);
    __loadFromFields(__fields);
  }

  public void parse(byte [] __record) throws RecordParser.ParseError {
    if (null == this.__parser) {
      this.__parser = new RecordParser(__inputDelimiters);
    }
    List<String> __fields = this.__parser.parseRecord(__record);
    __loadFromFields(__fields);
  }

  public void parse(char [] __record) throws RecordParser.ParseError {
    if (null == this.__parser) {
      this.__parser = new RecordParser(__inputDelimiters);
    }
    List<String> __fields = this.__parser.parseRecord(__record);
    __loadFromFields(__fields);
  }

  public void parse(ByteBuffer __record) throws RecordParser.ParseError {
    if (null == this.__parser) {
      this.__parser = new RecordParser(__inputDelimiters);
    }
    List<String> __fields = this.__parser.parseRecord(__record);
    __loadFromFields(__fields);
  }

  public void parse(CharBuffer __record) throws RecordParser.ParseError {
    if (null == this.__parser) {
      this.__parser = new RecordParser(__inputDelimiters);
    }
    List<String> __fields = this.__parser.parseRecord(__record);
    __loadFromFields(__fields);
  }

  private void __loadFromFields(List<String> fields) {
    Iterator<String> __it = fields.listIterator();
    String __cur_str = null;
    try {
    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.employeeno = null; } else {
      this.employeeno = new java.math.BigDecimal(__cur_str);
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.ename = null; } else {
      this.ename = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.job = null; } else {
      this.job = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.hiredate = null; } else {
      this.hiredate = java.sql.Date.valueOf(__cur_str);
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.sal = null; } else {
      this.sal = new java.math.BigDecimal(__cur_str);
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.departmentno = null; } else {
      this.departmentno = new java.math.BigDecimal(__cur_str);
    }

    } catch (RuntimeException e) {    throw new RuntimeException("Can't parse input data: '" + __cur_str + "'", e);    }  }

  private void __loadFromFields0(Iterator<String> __it) {
    String __cur_str = null;
    try {
    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.employeeno = null; } else {
      this.employeeno = new java.math.BigDecimal(__cur_str);
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.ename = null; } else {
      this.ename = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.job = null; } else {
      this.job = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.hiredate = null; } else {
      this.hiredate = java.sql.Date.valueOf(__cur_str);
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.sal = null; } else {
      this.sal = new java.math.BigDecimal(__cur_str);
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.departmentno = null; } else {
      this.departmentno = new java.math.BigDecimal(__cur_str);
    }

    } catch (RuntimeException e) {    throw new RuntimeException("Can't parse input data: '" + __cur_str + "'", e);    }  }

  public Object clone() throws CloneNotSupportedException {
    newemployee o = (newemployee) super.clone();
    o.hiredate = (o.hiredate != null) ? (java.sql.Date) o.hiredate.clone() : null;
    return o;
  }

  public void clone0(newemployee o) throws CloneNotSupportedException {
    o.hiredate = (o.hiredate != null) ? (java.sql.Date) o.hiredate.clone() : null;
  }

  public Map<String, Object> getFieldMap() {
    Map<String, Object> __sqoop$field_map = new HashMap<String, Object>();
    __sqoop$field_map.put("employeeno", this.employeeno);
    __sqoop$field_map.put("ename", this.ename);
    __sqoop$field_map.put("job", this.job);
    __sqoop$field_map.put("hiredate", this.hiredate);
    __sqoop$field_map.put("sal", this.sal);
    __sqoop$field_map.put("departmentno", this.departmentno);
    return __sqoop$field_map;
  }

  public void getFieldMap0(Map<String, Object> __sqoop$field_map) {
    __sqoop$field_map.put("employeeno", this.employeeno);
    __sqoop$field_map.put("ename", this.ename);
    __sqoop$field_map.put("job", this.job);
    __sqoop$field_map.put("hiredate", this.hiredate);
    __sqoop$field_map.put("sal", this.sal);
    __sqoop$field_map.put("departmentno", this.departmentno);
  }

  public void setField(String __fieldName, Object __fieldVal) {
    if (!setters.containsKey(__fieldName)) {
      throw new RuntimeException("No such field:"+__fieldName);
    }
    setters.get(__fieldName).setField(__fieldVal);
  }

}
