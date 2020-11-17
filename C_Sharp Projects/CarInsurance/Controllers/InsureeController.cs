using System;
using System.Collections.Generic;
using System.Data;
using System.Data.Entity;
using System.Linq;
using System.Net;
using System.Web;
using System.Web.Mvc;
using CarInsurance.Models;
using CarInsurance.ViewModels;

namespace CarInsurance.Controllers
{
    public class InsureeController : Controller
    {
        private InsuranceEntities db = new InsuranceEntities();

        // GET: Insuree
        public ActionResult Index()
        {
            return View(db.Tables.ToList());
        }

        // GET: Insuree/Details/5
        public ActionResult Details(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            Table table = db.Tables.Find(id);
            if (table == null)
            {
                return HttpNotFound();
            }
            return View(table);
        }

        // GET: Insuree/Create
        public ActionResult Create()
        {
            return View();
        }

        // POST: Insuree/Create
        // To protect from overposting attacks, enable the specific properties you want to bind to, for 
        // more details see https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create([Bind(Include = "Id,FirstName,LastName,EmailAddress,DateOfBirth,CarYear,CarMake,CarModel,DUI,SpeedingTickets,CoverageType,Quote")] Table table)
        {

            if (ModelState.IsValid)
            {
                DateTime now = DateTime.Now;
                int current = now.Year;
                int dob = table.DateOfBirth.Year;
                int age = current - dob;
                var make = table.CarMake.ToLower();
                var model = table.CarModel.ToLower();
                table.Quote = 50;
                if (age < 18)
                {
                    table.Quote += 100;
                }
                else if (age >= 18 && age < 26)
                {
                    table.Quote += 50;
                }
                else
                {
                    table.Quote += 25;
                }
                if (table.CarYear < 2000)
                {
                    table.Quote += 25;
                }
                if (table.CarYear > 2015)
                {
                    table.Quote += 25;
                }
                if (make == "porsche")
                {
                    table.Quote += 25;
                }
                if (make == "porsche" && model == "911 carrera")
                {
                    table.Quote += 25;
                }
                if (table.SpeedingTickets > 0)
                {
                    table.Quote += table.SpeedingTickets * 10;
                }
                if (table.DUI)
                {
                    table.Quote += table.Quote * .25m;
                }
                if (table.CoverageType)
                {
                    table.Quote += table.Quote * .5m;
                }
                db.Tables.Add(table);
                db.SaveChanges();
                return RedirectToAction("Index");
            }

            return View(table);
        }

        // GET: Insuree/Edit/5
        public ActionResult Edit(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            Table table = db.Tables.Find(id);
            if (table == null)
            {
                return HttpNotFound();
            }
            return View(table);
        }

        // POST: Insuree/Edit/5
        // To protect from overposting attacks, enable the specific properties you want to bind to, for 
        // more details see https://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit([Bind(Include = "Id,FirstName,LastName,EmailAddress,DateOfBirth,CarYear,CarMake,CarModel,DUI,SpeedingTickets,CoverageType,Quote")] Table table)
        {
            if (ModelState.IsValid)
            {
                db.Entry(table).State = EntityState.Modified;
                db.SaveChanges();
                return RedirectToAction("Index");
            }
            return View(table);
        }

        // GET: Insuree/Delete/5
        public ActionResult Delete(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            Table table = db.Tables.Find(id);
            if (table == null)
            {
                return HttpNotFound();
            }
            return View(table);
        }

        // POST: Insuree/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public ActionResult DeleteConfirmed(int id)
        {
            Table table = db.Tables.Find(id);
            db.Tables.Remove(table);
            db.SaveChanges();
            return RedirectToAction("Index");
        }

        protected override void Dispose(bool disposing)
        {
            if (disposing)
            {
                db.Dispose();
            }
            base.Dispose(disposing);
        }

        public ActionResult Admin(int? id)
        {
            using (InsuranceEntities db = new InsuranceEntities())
            {
                var tables = db.Tables.Where(x => x.Id != null).ToList();
                var tableVms = new List<TableVm>();
                foreach (var x in tables)
                {
                    var tableVm = new TableVm();
                    tableVm.FirstName = x.FirstName;
                    tableVm.LastName = x.LastName;
                    tableVm.EmailAddress = x.EmailAddress;
                    tableVm.Quote = x.Quote;

                    tableVms.Add(tableVm);
                }
                return View(tableVms);
            }
        }
    }
}
